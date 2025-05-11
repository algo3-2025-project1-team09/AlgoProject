# test_simulation.py
from game_controller import GameController
import time

class TestSimulation(GameController):
    def start_game(self):
        self.logger.log_event("[DEBUG] Starting test simulation")
        self.logger.start()
        self.initialize_factions(2)
        self.logger.log_event(f"[DEBUG] Initialized {len(self.factions)} factions")

        for faction in self.factions:
            faction.deploy_initial_units(melee_count=2, ranged_count=2)
            for unit in faction.units:
                self.logger.log_event(f"[INIT] {unit.__class__.__name__} from {faction.name} at ({unit.x},{unit.y})")
            faction.start_units()

        print("\n[TEST] Running simulation for 10 seconds...\n", flush=True)
        start = time.time()
        tick = 0
        while time.time() - start < 10:
            self.logger.log_event(f"[TEST] Tick {tick}")
            self.battlefield.print_map()
            time.sleep(2)
            tick += 1

        self.logger.log_event("[TEST] Simulation complete.")
        self.shutdown()

if __name__ == "__main__":
    TestSimulation().start_game()
