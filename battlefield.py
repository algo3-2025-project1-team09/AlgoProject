import threading

class Battlefield:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        self.lock = threading.RLock()

    def is_within_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def is_tile_free(self, x, y):
        with self.lock:
            return self.is_within_bounds(x, y) and self.grid[y][x] is None

    def place_unit(self, unit, x, y):
        with self.lock:
            if self.is_tile_free(x, y):
                self.grid[y][x] = unit
                return True
            return False

    def move_unit(self, unit, old_x, old_y, new_x, new_y):
        with self.lock:
            if self.is_tile_free(new_x, new_y):
                self.grid[old_y][old_x] = None
                self.grid[new_y][new_x] = unit
                return True
            return False

    def remove_unit(self, x, y):
        with self.lock:
            self.grid[y][x] = None

    def get_units_around(self, x, y, range_=1):
        nearby = []
        with self.lock:
            for dx in range(-range_, range_ + 1):
                for dy in range(-range_, range_ + 1):
                    nx, ny = x + dx, y + dy
                    if self.is_within_bounds(nx, ny) and self.grid[ny][nx]:
                        nearby.append(self.grid[ny][nx])
        return nearby

    def print_map(self):
        with self.lock:
            print("Battlefield State:", flush=True)
            for row in self.grid:
                print(" ".join(unit.symbol if unit else '.' for unit in row), flush=True)
            print("\n", flush=True)
