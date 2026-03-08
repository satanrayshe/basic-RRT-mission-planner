import matplotlib.pyplot as plt
from simulator import Simulator
import viz

def main():
    sim = Simulator()
    plt.ion()

    try:
        print("Starting Simulation...")
        for step in range(100):
            nodes, threat_pos = sim.run_step()

            viz.render(nodes, threat_pos, sim.threat_vel[0] if hasattr(sim, 'threat_vel') else 2.0)

            plt.pause(0.05)

    except KeyboardInterrupt:
        print("\nSimulation terminated by user.")
    finally:
        plt.ioff()
        plt.show()

if __name__ == "__main__":
    main()
