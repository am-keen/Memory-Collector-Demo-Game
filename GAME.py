# ==============================================================================
# GAME DEMO: The Memory Collector
# Module 1: Execution Order, State Tracking, and Dynamic Mechanics
# ==============================================================================

# STEP 1: IMPORTS (Tools brought in first)
import random

# STEP 2: GAME STATE (Variables created BEFORE the loop uses them)
station_energy = 100
archived_memories = []
station_active = True

# STEP 3: INTRO BANNER & CALLSIGN
print("=== ARCHIVE STATION 7: MEMORY CORE ===")
archivist_id = input("Enter Archivist Callsign: ")

print(f"\nWelcome, Archivist {archivist_id}. Memory containment grid online.")
print(f"Station Energy: {station_energy}%")

# STEP 4: MAIN SCENE LOOP
while station_active:
    print("\n----------------------------------------")
    print(f"[Archivist: {archivist_id}] Energy: {station_energy}% | Archived: {len(archived_memories)}")
    print("----------------------------------------")
    
    # Presenting a memory fragment to process
    print("NEW MEMORY DETECTED: 'A forgotten childhood summer by the ocean'")
    print("What will you do?")
    print("1. Archive Memory (Cost: 15 Energy + Volatility Risk)")
    print("2. Erase Memory (Cost: 5 Energy)")
    print("3. Inspect Station Status")

    choice = input("Enter command (1, 2, or 3): ")

    # CHOICE 1: ARCHIVE
    if choice == "1":
        station_energy -= 15
        archived_memories.append("Childhood Summer")
        print("\n>> Memory successfully preserved in glass sphere.")
        
        # Calculate volatility (risk check)
        volatility = random.randint(1, 10)
        print(f">> Volatility Roll: {volatility}/10")
        
        if volatility > 7:
            print("WARNING! Emotional feedback surge! Station takes 10 extra damage!")
            station_energy -= 10

    # CHOICE 2: ERASE
    elif choice == "2":
        station_energy -= 5
        print("\n>> Memory purged into static. It fades completely.")

    # CHOICE 3: INSPECT
    elif choice == "3":
        print(f"\n[STATION LOG]: Archived Items ({len(archived_memories)}): {archived_memories}")
        print(f"[ENERGY RESERVES]: {station_energy}%")

    else:
        print("\nInvalid command. Systems awaiting 1, 2, or 3.")

    # CHECK END CONDITION 1: Energy Depleted (Loss)
    if station_energy <= 0:
        print("\n========================================")
        print("CRITICAL ERROR: Station power depleted! Core shutting down.")
        print("========================================")
        station_active = False

    # CHECK END CONDITION 2: Quota Reached (Victory)
    if len(archived_memories) == 3:
        print("\n========================================")
        print("QUOTA COMPLETE: 3 memories successfully archived!")
        print("========================================")
        station_active = False

# STEP 5: POST-LOOP OUTCOME
if station_energy > 0:
    print(f"\nExcellent work, Archivist {archivist_id}. Your shift is complete.")