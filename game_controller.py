import threading
import time
from battlefield import Battlefield
from faction import Faction
from logger import Logger
from command_handler import CommandHandler

class GameController:
    def __init__(self):
        self.battlefield = Battlefield()
        self.factions = []
        self.logger = Logger()
        self.command_handler = CommandHandler(self)
        self.is_running = True

    def initialize_factions(self, num_factions):
        for i in range(num_factions):
            faction = Faction(f"Faction_{chr(65+i)}", self.battlefield, self.logger)
            self.factions.append(faction)
    
    def start_game(self):
        self.logger.start()
        self.command_handler.start()
        self.initialize_factions(4)  # Example: 4 factions

        for faction in self.factions:
            faction.deploy_initial_units()

        # Start all unit threads
        for faction in self.factions:
            faction.start_units()

        # Main game loop
        while self.is_running:
            self.battlefield.print_map()
            time.sleep(5)

            if self.check_victory_condition():
                self.is_running = False
                winner = [f.name for f in self.factions if f.has_units()]
                if winner:
                    self.logger.log_event(f"[{winner[0]}] wins the battle!")
                else:
                    self.logger.log_event("No factions left. It's a draw!")

        self.shutdown()

    def check_victory_condition(self):
        alive_factions = [f for f in self.factions if f.has_units()]
        return len(alive_factions) <= 1
    
    def shutdown(self):
        self.logger.stop()
        self.command_handler.stop()
        for faction in self.factions:
            faction.stop_units()