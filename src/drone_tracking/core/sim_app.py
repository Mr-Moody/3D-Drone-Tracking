import os
import sys

from isaacsim import SimulationApp

class IsaacSimApp():
    """
    Wrapper for the Isaac Sim SimulationApp to manage startup, stepping, and shutdown.
    """
    def __init__(self, headless: bool = False, width: int = 1280, height: int = 720):
        # Automatically accepts EULA
        os.environ["OMNI_KIT_ACCEPT_EULA"] = "YES"
        
        config = {
            "headless": headless,
            "width": width,
            "height": height,
            "window_width": width + 100,
            "window_height": height + 100,
        }
        
        self.app = SimulationApp(config)
        
        # Import core Isaac utilities
        from omni.isaac.core.utils.extensions import enable_extension
        
        # Enable essential extensions
        enable_extension("omni.isaac.core")
        enable_extension("omni.isaac.debug_draw")

    def is_running(self) -> bool:
        """Checks if the simulation window is still open and active."""
        return self.app.is_running()

    def update(self):
        """Steps the physics and rendering by one frame."""
        self.app.update()

    def close(self):
        """Cleanly shuts down the simulation."""
        self.app.close()

# Singleton instance so that we don't open multiple simulation apps at a time
_instance = None

def get_app(**kwargs) -> IsaacSimApp:
    global _instance
    
    if _instance is None:
        _instance = IsaacSimApp(**kwargs)
        
    return _instance