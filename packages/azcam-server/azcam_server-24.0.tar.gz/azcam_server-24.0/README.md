# AzCam Server

*azcam-server* is the main server application for the *azcam* acquisition and analysis package. It usually runs in an IPython window and is mainly used to control data acquistion. 

## Documentation

See https://azcam.readthedocs.io/.

## Installation

`pip install azcam-server`

Or download the latest version from from github: https://github.com/mplesser/azcam-server.git.

## Configuration and startup 

An example code snippet to start an *azcamserver* process is:

```
ipython -m azcam_server.server_mock --profile azcamserver  -i
```

and then in the IPython window:

```python
instrument.set_wavelength(450)
wavelength = instrument.get_wavelength()
print(f"Current wavelength is {wavelength}")
exposure.expose(2., 'flat', "a 450 nm flat field image")
```

## Observe tool script example

Import observe for observing command use:
```
from azcam_server.tools.observe.observe import Observe
```

```
# this is a single line comment python style
```

This block shows some direct commands
```
observe = Observe()
observe.test(et=1.0,object="flat", filter="400")
observe.comment("a different new comment 123")
observe.delay(1)
observe.obs(et=2.0,object="zero", filter="400", dec="12:00:00.23", ra="-23:34:2.1")
```

This block shows an example of commands using python flow control
```
alt_start = 0.0
step_size = 0.01
num_steps = 100
for count in range(num_steps):
    altitude = alt_start + count*step_size
    observe.steptel(altitude=altitude)
    print(f"On loop {count} altitude is {altitude}")
```