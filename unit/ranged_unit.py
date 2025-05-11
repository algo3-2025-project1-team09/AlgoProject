import random
from unit.unit import Unit

class RangedUnit(Unit):
    def act(self):
        enemies = [u for u in self.battlefield.get_units_around(self.x, self.y, 2) if u.faction != self.faction]
        if enemies:
            target = random.choice(enemies)
            target.take_damage(10)
            self.logger.log_event(f"[{self.faction.name}] Ranged Unit at ({self.x}, {self.y}) attacked [{target.faction.name}] at ({target.x}, {target.y})")
        else:
            self.move()

    def move(self):
        dx, dy = random.choice([(0,1), (1,0), (0,-1), (-1,0)])
        new_x, new_y = self.x + dx, self.y + dy
        if self.battlefield.move_unit(self, self.x, self.y, new_x, new_y):
            self.logger.log_event(f"[{self.faction.name}] Ranged Unit moved from ({self.x}, {self.y}) to ({new_x}, {new_y})")
            self.x, self.y = new_x, new_y