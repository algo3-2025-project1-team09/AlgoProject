import random
from unit.melee_unit import MeleeUnit
from unit.ranged_unit import RangedUnit

class Faction:
    def __init__(self, name, battlefield, logger):
        self.name = name
        self.battlefield = battlefield
        self.logger = logger
        self.units = []
        self.symbol = name[-1] # Use the last character of the name as the symbol

    def deploy_initial_units(self, melee_count=2, ranged_count=2):
        for _ in range(melee_count):
            self.spawn_unit(MeleeUnit)
        for _ in range(ranged_count):
            self.spawn_unit(RangedUnit)

    def spawn_unit(self, unit_cls):
        for _ in range(100):  # Try 100 times to find a free tile
            x, y = random.randint(0, self.battlefield.width - 1), random.randint(0, self.battlefield.height - 1)
            if self.battlefield.is_tile_free(x, y):
                try:
                    unit = unit_cls(self, x, y)
                    self.battlefield.place_unit(unit, x, y)
                    self.units.append(unit)
                    self.logger.log_event(f"[SPAWN] {unit.__class__.__name__} created at ({x},{y}) for {self.name}")
                    return
                except Exception as e:
                    self.logger.log_event(f"[ERROR] Failed to spawn {unit_cls.__name__} at ({x},{y}): {e}")
    
    def start_units(self):
        for unit in self.units:
            unit.start()

    def stop_units(self):
        for unit in self.units:
            unit.stop()

    def has_units(self):
        return any(unit.is_alive() for unit in self.units)