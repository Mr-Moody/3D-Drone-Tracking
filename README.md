# 3D-Drone-Tracking
Pipeline to detect and track the 3D position of a single flying drone using an array of RGBD cameras. The drone will change altitude, distance, and orientation across the sky with varying backgrounds and lighting following defined paths. This system is built on the Pegasus simulator for NVIDIA Isaac Sim.

## Installation

### uv environment
Create a new uv virtual environment with Python 3.11:
```bash
uv venv --python 3.11
```

Activate the uv environment with:
```bash
.venv\Scripts\activate
```

### Isaac Sim
Install the python package into uv using:
```bash
uv add "isaacsim[all,extscache]" --index https://pypi.nvidia.com
```
> note this can take upwards of 10 mins to complete.

Verify installation with:
```bash
uv run isaacsim
```

> If this fails, then make sure that isaacsim is set to use your dedicated GPU. In windows go to: Settings > System > Display > Graphics > Add desktop app. Add the python.exe file inside .venv to the list of applications, and set GPU preference to High Performace (your GPU). Rerun with ```uv run isaacsim --reset-user```

Add Isaac Sim to path by:
- Getting path:
```bash
uv run python -c "import isaacsim; print(isaacsim.__path__[0])" 
```

- Adding path:
```bash
$env:ISAACSIM_PATH = "your path"
```
> This could look like ```$env:ISAACSIM_PATH = "C:\3D-Drone-Tracking\.venv\Lib\site-packages\isaacsim"```

### Pegasus Simulator

Clone repository into project root directory:
```bash
git clone https://github.com/PegasusSimulator/PegasusSimulator.git
```

Add project to uv venv:
```bash
uv pip install -e ./PegasusSimulator/extensions/pegasus.simulator
```

Verify pegasus installation with:

```bash
uv run python tests\verify_pegasus.py
```