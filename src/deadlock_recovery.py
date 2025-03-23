def recover_deadlock(deadlocked_processes, allocation, available):
    """
    Recovers from deadlock by preempting resources from deadlocked processes.
    """
    if not deadlocked_processes:
        return "No Deadlock Detected. No Recovery Needed."

    print(f"Deadlocked Processes: {deadlocked_processes}")
    for process in deadlocked_processes:
        print(f"Preempting resources from {process}...")
        available = [available[j] + allocation[process][j] for j in range(len(available))]
    
    return f"Resources reallocated. Available Resources: {available}"
