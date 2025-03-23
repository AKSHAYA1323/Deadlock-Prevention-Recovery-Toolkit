def recover_deadlock(deadlocked_processes, allocation, available):
    """
    Recovers from deadlock by preempting resources from deadlocked processes.
    Returns updated available resources after recovery.
    """
    if not deadlocked_processes:
        return available  # No deadlock, return current available resources

    print(f"Deadlocked Processes: {deadlocked_processes}")
    for process in deadlocked_processes:
        if process in allocation:
            print(f"Preempting resources from {process}...")
            available = [available[j] + allocation[process][j] for j in range(len(available))]
        else:
            print(f"Error: Process {process} not found in allocation table.")

    print(f"Resources reallocated. Available Resources: {available}")
    return available
