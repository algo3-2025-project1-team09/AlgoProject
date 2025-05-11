import threading

class CommandHandler:
    def __init__(self, controller):
        self.controller = controller
        self.running = False
        self.thread = threading.Thread(target=self._run, daemon=True)
        
    def start(self):
        self.running = True
        self.thread.start()
        
    def stop(self):
        self.running = False
        self.thread.join()

    def _run(self):
        while self.running:
            try:
                command = input("Enter command: ")
                if command == "status":
                    self.print_status()
                elif command.startswith("spawn"):
                    self.handle_spawn(command)
            except Exception as e:
                print(f"Command error: {e}")

    def print_status(self):
        for faction in self.controller.factions:
            print(f"{faction.name}:")
            for unit in faction.units:
                if unit.is_alive():
                    print(f"  {unit.__class__.__name__} at ({unit.x}, {unit.y}), HP: {unit.health}")

    def handle_spawn(self, command):
            try:
                parts = command.split()
                if len(parts) != 4:
                    print("Usage: spawn <count> <faction_index> <melee|ranged>")
                    return

                if not parts[1].isdigit() or not parts[2].isdigit():
                    print("Error: count and faction_index must be integers")
                    return

                count = int(parts[1])
                faction_index = int(parts[2])
                unit_type = parts[3]

                if faction_index >= len(self.controller.factions):
                    print("Invalid faction index")
                    return

                if unit_type not in ("melee", "ranged"):
                    print("Unit type must be 'melee' or 'ranged'")
                    return

                faction = self.controller.factions[faction_index]
                from unit.melee_unit import MeleeUnit
                from unit.ranged_unit import RangedUnit
                unit_cls = MeleeUnit if unit_type == "melee" else RangedUnit

                for _ in range(count):
                    faction.spawn_unit(unit_cls)
                faction.start_units()

            except Exception as e:
                print(f"Unexpected error: {e}")