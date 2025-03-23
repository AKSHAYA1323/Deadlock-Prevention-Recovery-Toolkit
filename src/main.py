from deadlock_prevention import is_safe
from deadlock_detection import detect_deadlock
from deadlock_recovery import recover_deadlock

# Define processes and resources
processes = ['P1', 'P2', 'P3']
available = [3, 3, 2]  # Example available resources
allocation = {
    'P1': [0, 1, 0],
    'P2': [2, 0, 0],
    'P3': [3, 0, 3]
}
max_demand = {
    'P1': [7, 5, 3],
    'P2': [3, 2, 2],
    'P3': [9, 0, 2]
}
request = {
    'P1': [1, 0, 2],
    'P2': [0, 1, 0],
    'P3': [3, 0, 3]
}

# Step 1: Deadlock Prevention
print("\n🔹 Running Deadlock Prevention...")
safe_sequence = is_safe(processes, allocation, max_demand, available)
if safe_sequence:
    print(f"Safe Sequence Found: {safe_sequence}")
else:
    print("Deadlock Prevention Failed. Proceeding to Detection.")

    # Step 2: Deadlock Detection
    print("\n🔹 Running Deadlock Detection...")
    deadlocked_processes = detect_deadlock(processes, allocation, available, request)
    
    if deadlocked_processes:
        print(f"Deadlocked Processes: {deadlocked_processes}")

        # Step 3: Deadlock Recovery
        print("\n🔹 Running Deadlock Recovery...")
        available = recover_deadlock(deadlocked_processes, allocation, available)
    else:
        print("No Deadlock Detected. System is Safe.")
