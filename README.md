# README.md
# Async Strategy Battle

A real-time strategy game simulation with concurrent unit behavior.

By BREGLIA Francesco and VALI Uku

## Features
- Asynchronous unit logic using threads
- Real-time map printing every 5 seconds
- Custom user commands for inspecting status or spawning units
- Logger system writing game events to `battle_log.txt`

## How to Run
1. Ensure you have Python 3.10+ installed
2. Run the game:
   ```bash
   python main.py
   ```

## Available Commands
- `status` — show health and position of all units
- `spawn <count> <faction_index> <melee|ranged>` — spawn units for a faction
  Example:
  ```
  spawn 3 0 melee
  spawn 2 1 ranged
  ```

## Log Output
All game events are logged to `battle_log.txt` in real time.

## Project Structure
```
async_strategy_battle/
├── main.py
├── game_controller.py
├── battlefield.py
├── faction.py
├── logger.py
├── command_handler.py
├── unit/
│   ├── __init__.py
│   ├── unit.py
│   ├── melee_unit.py
│   └── ranged_unit.py
└── battle_log.txt
```
