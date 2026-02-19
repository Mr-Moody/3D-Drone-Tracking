import os

# Force headless if you just want to check the import without opening a window
os.environ["OMNI_KIT_ACCEPT_EULA"] = "YES"

# Start the simulation application
from isaacsim import SimulationApp
simulation_app = SimulationApp({"headless": True})

# Import Pegasus or pxr
try:
    import pxr
    import pegasus.simulator
    print(" Success: Pegasus and PXR (USD) are ready!")
except ImportError as e:
    print(f"Still missing a module: {e}")

simulation_app.close()