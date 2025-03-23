from deadlock_prevention import is_safe
from deadlock_detection import detect_deadlock
from deadlock_recovery import recover_deadlock

def main():
    num_processes = int(input("Enter the number of processes: "))
    num_resources = int(input("Enter the number of resource types: "))

    processes = [f"P{i+1}" for i in range(num_processes)]
    allocation = []
    max_demand = []

    print("\nEnter Allocation Matrix:")
    for i in range(num_processes):
        allocation.append(list(map(int, input(f"Process {processes[i]}: ").split())))

    print("\nEnter Maximum Demand Matrix:")
    for i in range(num_processes):
        max_demand.append(list(map(int, input(f"Process {processes[i]}: ").split())))

    available = list(map(int, input("\nEnter Available Resources: ").split()))

    # Deadlock Prevention
    print("\n🔹 Running Deadlock Prevention...")
    is_safe_state, safe_sequence = is_safe(processes, allocation, max_demand, available)

    if is_safe_state:
        print(f"✅ Safe Sequence Found: {safe_sequence}")
        return
    else:
        print("❌ Deadlock Prevention Failed. Proceeding to Detection.")

    # Deadlock Detection
    print("\n🔹 Running Deadlock Detection...")
    deadlocked_processes = detect_deadlock(processes, allocation, max_demand, available)

    if deadlocked_processes:
        print(f"⚠️ Deadlocked Processes: {deadlocked_processes}")
    else:
        print("✅ No Deadlock Detected.")
        return

    # Deadlock Recovery
    print("\n🔹 Running Deadlock Recovery...")
    available, recovery_message = recover_deadlock(deadlocked_processes, allocation, available)
    print(recovery_message)


if __name__ == "__main__":
    main()
