from drone_tracking.core import app, DroneEnvironment

def main():
    # Instantiate the world (sets up Pegasus and the Drone)
    env = DroneEnvironment()

    print("Starting Simulation Loop...")
    
    # Uses the app instance from core
    while app.is_running():
        # Update the drone environment
        env.update()
        
        # Step the Isaac Sim engine
        app.update()

    # Clean shutdown
    app.close()

if __name__ == "__main__":
    main()