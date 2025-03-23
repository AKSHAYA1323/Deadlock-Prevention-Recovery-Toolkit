def recover_deadlock(deadlocked_processes, allocation, available):
    """
    Recovers from deadlock by preempting resources from deadlocked processes.
    """
    if not deadlocked_processes:
        return "No Deadlock Detected. No Recovery Needed."

    print(f"Deadlocked Processes: {deadlocked_processes}")

    for process in deadlocked_processes:
        process_index = int(process[1:])  # Extract index from process name (e.g., "P1" -> 1)
        
        print(f"Preempting resources from {process}...")

        # Ensure process index is within range
        if process_index >= len(allocation):
            print(f"Error: Process {process} index out of range.")
            continue
        
        # Update available resources
        available = [available[j] + allocation[process_index][j] for j in range(len(available))]

    return f"Resources reallocated. Available Resources: {available}"
