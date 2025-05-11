import threading
import time
import random
from abc import ABC, abstractmethod

class Unit(threading.Thread, ABC):
    def __init__(self, faction, x, y, health=100):
        super().__init__()
        self.faction = faction
        self.x = x
        self.y = y
        self.health = health
        self.alive = True
        self.battlefield = faction.battlefield
        self.symbol = faction.symbol
        self.logger = faction.logger
        self.daemon = True  # Set the thread as a daemon thread

    def run(self):
        while self.alive:
            self.act()
            time.sleep(1)

    def is_alive(self):
        return self.alive and self.health > 0
    
    def stop(self):
        self.alive = False

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.die()

    def die(self):
        self.alive = False
        self.battlefield.remove_unit(self.x, self.y)
        self.logger.log_event(f"[{self.faction.name}] {self.__class__.__name__} at ({self.x}, {self.y}) has died.")

    @abstractmethod
    def act(self):
        pass