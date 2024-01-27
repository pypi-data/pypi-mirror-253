"""
azcamserver script for a mock system.

Command line options:
  -system azcam_mock
  -datafolder path_to_datafolder
  -cmdport azcamserver_port
"""

import os
import sys

import azcam
import azcam_server.server
from azcam.scripts import loadscripts

from azcam.logger import check_for_remote_logger

from azcam_server.tools.queue import Queue
from azcam_server.tools.controller import Controller
from azcam_server.tools.instrument import Instrument
from azcam_server.tools.tempcon import TempCon
from azcam_server.tools.display import Display
from azcam_server.tools.telescope import Telescope
from azcam_server.tools.exposure import Exposure
from azcam_server.cmdserver import CommandServer
from azcam_server.tools.focus import Focus
import azcam_server.shortcuts

from azcam_webtools.webserver.fastapi_server import WebServer
from azcam_webtools.status.status import Status
from azcam_webtools.exptool.exptool import Exptool

# ****************************************************************
# parse command line arguments
# ****************************************************************
try:
    i = sys.argv.index("-system")
    systemname = sys.argv[i + 1]
except ValueError:
    systemname = "azcam_mock"
try:
    i = sys.argv.index("-datafolder")
    datafolder = sys.argv[i + 1]
except ValueError:
    datafolder = None
try:
    i = sys.argv.index("-cmdport")
    cmdport = int(sys.argv[i + 1])
except ValueError:
    cmdport = 2402


def setup():
    global systemname, datafolder, cmdport
    azcam.db.systemname = systemname
    azcam.db.systemfolder = os.path.dirname(__file__)
    azcam.db.systemfolder = azcam.utils.fix_path(azcam.db.systemfolder)

    if datafolder is None:
        droot = os.environ.get("AZCAM_DATAROOT")
        if droot is None:
            if os.name == "posix":
                droot = os.environ.get("HOME")
            else:
                droot = "/"
            azcam.db.datafolder = os.path.join(
                os.path.realpath(droot), "data", azcam.db.systemname
            )
        else:
            azcam.db.datafolder = os.path.join(
                os.path.realpath(droot), azcam.db.systemname
            )
    else:
        azcam.db.datafolder = os.path.realpath(datafolder)

    azcam.db.servermode = azcam.db.systemname
    azcam.db.verbosity = 2

    # ****************************************************************
    # parameter file
    # ****************************************************************
    parfile = os.path.join(
        azcam.db.datafolder, "parameters", "parameters_server_mock.ini"
    )
    azcam.db.parameters.read_parfile(parfile)
    azcam.db.parameters.update_pars("azcamserver")

    # ****************************************************************
    # logging
    # ****************************************************************
    logfile = os.path.join(azcam.db.datafolder, "logs", "server.log")
    if check_for_remote_logger():
        azcam.db.logger.start_logging(logtype="23", logfile=logfile)
    else:
        azcam.db.logger.start_logging(logtype="1", logfile=logfile)

    # message
    azcam.log(f"Configuring {azcam.db.systemname}")

    # define command server
    cmdserver = CommandServer()
    cmdserver.port = cmdport
    cmdserver.logcommands = 0

    # ****************************************************************
    # tools
    # ****************************************************************
    controller = Controller()
    instrument = Instrument()
    instrument.enabled = 0
    telescope = Telescope()
    telescope.enabled = 0
    tempcon = TempCon()
    tempcon.enabled = 0
    display = Display()
    exposure = Exposure()
    observe = Observe()
    focus = Focus()

    # ****************************************************************
    # scripts
    # ****************************************************************
    azcam.log("Loading azcam_server.scripts")
    loadscripts(["azcam_server.scripts"])

    # ****************************************************************
    # web server
    # ****************************************************************
    if 0:
        webserver = WebServer()
        webserver.port = 2403
        webserver.logcommands = 0
        webserver.logstatus = 0
        webserver.index = os.path.join(azcam.db.systemfolder, "index.html")
        webserver.message = f"for host {azcam.db.hostname}"
        webserver.datafolder = azcam.db.datafolder
        webserver.start()

        webstatus = Status()
        webstatus.message = "for a mock system"
        webstatus.initialize()

        exptool = Exptool()
        exptool.initialize()

        # queue = Queue()
        # queue.initialize()

        azcam.log("Started web apps")

    # ****************************************************************
    # start command server
    # ****************************************************************
    azcam.log(f"Starting cmdserver - listening on port {cmdserver.port}")
    cmdserver.start()


setup()
from azcam.cli import *
