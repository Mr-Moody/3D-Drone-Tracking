import os
import sys

# Do NOT import omni at top level: Omniverse APIs are only available after SimulationApp() runs.
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
        
        # Imports only after SimulationApp() has started the Omniverse runtime
        from omni.isaac.core.utils.extensions import enable_extension, disable_extension
        import omni.kit.app

        # Enable essential extensions (isaacsim.gui.components required by Procedural Forest extension on Isaac Sim 5)
        enable_extension("omni.isaac.core")
        enable_extension("omni.isaac.debug_draw")
        enable_extension("isaacsim.gui.components")

        ext_manager = omni.kit.app.get_app().get_extension_manager()
        # Try env override, then Procedural, then Procedual (repo name typo on GitHub)
        forest_path = os.environ.get("FOREST_EXTENSION_PATH")
        if not forest_path or not os.path.isdir(forest_path):
            forest_path = os.path.abspath("C:/Robotics/Nvidia-Isaac-Sim-Procedural-Forest-Generator/exts")
        if not os.path.isdir(forest_path):
            forest_path = os.path.abspath("C:/Robotics/Nvidia-Isaac-Sim-Procedual-Forest-Generator/exts")
        if os.path.isdir(forest_path):
            try:
                ext_manager.add_path(forest_path)
            except TypeError:
                import omni.ext._extensions as _ext
                ext_manager.add_path(forest_path, _ext.ExtensionPathType.USER)
            try:
                enable_extension("company.hello.world")
            except Exception:
                pass
        # Disable ROS2 bridge
        disable_extension("omni.isaac.ros2_bridge")

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