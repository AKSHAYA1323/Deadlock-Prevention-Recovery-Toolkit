def recover_deadlock(deadlocked_processes, allocation, available):
    """
    Recovers from deadlock by preempting resources from deadlocked processes.
    """
    if not deadlocked_processes:
        return available, "No Deadlock Detected. No Recovery Needed."

    print(f"🔹 Deadlocked Processes: {deadlocked_processes}")
    for process in deadlocked_processes:
        index = int(process[1:]) - 1  # Extract numeric index from "P1", "P2", etc.
        if 0 <= index < len(allocation):
            print(f"Preempting resources from {process}...")
            available = [available[j] + allocation[index][j] for j in range(len(available))]
        else:
            print(f"Error: Process {process} not found in allocation table.")

    return available, f"Resources reallocated. Available Resources: {available}"
