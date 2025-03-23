from deadlock_detection import detect_deadlock
from deadlock_prevention import is_safe
from deadlock_recovery import recover_deadlock

def main():
    processes = ["P1", "P2", "P3"]
    available = [3, 3, 2]  
    allocation = [[0, 1, 0], [2, 0, 0], [3, 0, 2]]
    request = [[0, 0, 0], [2, 0, 2], [0, 0, 0]]
    max_demand = [[7, 5, 3], [3, 2, 2], [9, 0, 2]]

    print("\n🔹 Running Deadlock Detection...")
    deadlocks = detect_deadlock(processes, available, allocation, request)
    print(f"Deadlocked Processes: {deadlocks if deadlocks else 'No Deadlock Detected'}")

    print("\n🔹 Running Deadlock Prevention...")
    safe, sequence = is_safe(processes, available, max_demand, allocation)
    print(f"Safe Sequence: {sequence if safe else 'No Safe Sequence. Deadlock Prevention Failed'}")

    print("\n🔹 Running Deadlock Recovery...")
    print(recover_deadlock(deadlocks, allocation, available))

if __name__ == "__main__":
    main()
