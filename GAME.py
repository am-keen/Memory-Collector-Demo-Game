# ==============================================================================
# GAME DEMO: The Memory Collector (Updated with Memory Deck)
# ==============================================================================

import random

station_energy = 100
archived_memories = []
station_active = True

# A DECK OF UNIQUE MEMORIES TO PROCESS
available_memories = [
    "A forgotten childhood summer by the ocean",
    "The smell of rain on hot pavement in 1998",
    "A quiet midnight conversation over warm tea",
    "The glowing sign of an all-night diner",
    "Laughter echoing in an empty school hallway"
]

print("=== ARCHIVE STATION 7: MEMORY CORE ===")
archivist_id = input("Enter Archivist Callsign: ")

print(f"\nWelcome, Archivist {archivist_id}. Memory containment grid online.")

while station_active:
    print("\n----------------------------------------")
    print(f"[Archivist: {archivist_id}] Energy: {station_energy}% | Archived: {len(archived_memories)}/3")
    print("----------------------------------------")
    
    # Grab the current memory from the list
    current_memory = available_memories[0]
    print(f"NEW MEMORY DETECTED: '{current_memory}'")
    print("What will you do?")
    print("1. Archive Memory (Cost: 15 Energy + Volatility Risk)")
    print("2. Erase Memory (Cost: 5 Energy)")
    print("3. Inspect Station Status")

    choice = input("Enter command (1, 2, or 3): ")

    if choice == "1":
        station_energy -= 15
        # Add the specific memory name to archived_memories
        archived_memories.append(current_memory)
        # Remove it from the available deck so it doesn't repeat!
        available_memories.pop(0)
        
        print(f"\n>> Memory '{current_memory}' preserved in glass sphere.")
        
        volatility = random.randint(1, 10)
        print(f">> Volatility Roll: {volatility}/10")
        if volatility > 7:
            print("WARNING! Emotional feedback surge! Station takes 10 extra damage!")
            station_energy -= 10

    elif choice == "2":
        station_energy -= 5
        print(f"\n>> Memory '{current_memory}' purged into static.")
        # Remove the erased memory from the deck so a new one appears
        available_memories.pop(0)

    elif choice == "3":
        print(f"\n[STATION LOG]: Archived Items ({len(archived_memories)}): {archived_memories}")
        print(f"[ENERGY RESERVES]: {station_energy}%")

    else:
        print("\nInvalid command. Systems awaiting 1, 2, or 3.")

    # WIN / LOSS CHECKS
    if station_energy <= 0:
        print("\n========================================")
        print("CRITICAL ERROR: Station power depleted! Core shutting down.")
        print("========================================")
        station_active = False

    if len(archived_memories) == 3:
        print("\n========================================")
        print("QUOTA COMPLETE: 3 memories successfully archived!")
        print("========================================")
        station_active = False

if station_energy > 0:
    print(f"\nExcellent work, Archivist {archivist_id}. Your shift is complete.")
    print(f"Memories saved for humanity: {archived_memories}")