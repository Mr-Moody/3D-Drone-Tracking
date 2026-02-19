from .sim_app import get_app

# Initialises the simulation app on first import
app = get_app()

from .world import DroneEnvironment

__all__ = ["app", "DroneEnvironment"]