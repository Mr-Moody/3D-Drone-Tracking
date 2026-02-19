from omni.isaac.core.world import World

from pegasus.simulator.logic.interface.pegasus_interface import PegasusInterface
from pegasus.simulator.logic.vehicles.multirotor import Multirotor, MultirotorConfig
from pegasus.simulator.params import ROBOTS, SIMULATION_ENVIRONMENTS


def _get_forest_generator():
    """Import ForestGenerator from the Procedural Forest extension after the stage is ready."""
    try:
        from company.hello.world.forest_gen import ForestGenerator
        return ForestGenerator
    except ImportError:
        try:
            from company.hello.world import ForestGenerator
            return ForestGenerator
        except ImportError:
            return None


class DroneEnvironment():
    def __init__(self):
        self.pg = PegasusInterface()

        # Create the Isaac Sim World and attach to Pegasus before loading environment
        self.pg._world = World(**self.pg._world_settings)
        self.world = self.pg.world

        # Create the physics scene, ground plane, and skybox
        self.pg.load_environment(SIMULATION_ENVIRONMENTS["Curved Gridroom"])

        ForestGenerator = _get_forest_generator()
        
        if ForestGenerator is not None:
            self.forest_gen = ForestGenerator()

            if hasattr(self.forest_gen, "generate_forest"):
                self.forest_gen.generate_forest(
                    num_trees=40,
                    spawn_area=[30.0, 30.0],
                    seed=42
                )
                print("Procedural forest/terrain generated.")
        else:
            self.forest_gen = None
            print("Procedural Forest extension not available; skipping forest generation.")

        # Drone config
        config = MultirotorConfig()
        config.init_pos = [0.0, 0.0, 5.0]
        config.init_orientation = [0.0, 0.0, 0.0, 1.0]
        
        # Runs without PX4/MAVLink
        config.backends = []
        
        # Spawn the drone (stage_prefix, usd_file, vehicle_id, init_pos, init_orientation, config=)
        self.drone = Multirotor(
            "/World/Drones/Iris",
            ROBOTS["Iris"],
            0,
            config.init_pos,
            config.init_orientation,
            config=config,
        )

        # Reset so all articulations (e.g. the drone) are initialized
        self.world.reset()

        print("Drone Environment Initialised.")

    def update(self):
        """Step physics and rendering (Pegasus uses World.step, not PegasusInterface.update)."""
        self.world.step(render=True)