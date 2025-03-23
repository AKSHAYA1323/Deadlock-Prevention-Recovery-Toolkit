def is_safe(processes, allocation, max_demand, available):
    """
    Implements Banker's Algorithm to check if a system is in a safe state.
    Returns a safe sequence if possible; otherwise, returns None.
    """
    n = len(processes)  # Number of processes
    m = len(available)  # Number of resource types

    # Calculate the need matrix
    need = {p: [max_demand[p][j] - allocation[p][j] for j in range(m)] for p in processes}

    work = available[:]  # Available resources copy
    finish = {p: False for p in processes}  # Mark all processes as unfinished
    safe_sequence = []  # Store safe sequence

    while len(safe_sequence) < n:
        found = False
        for p in processes:
            if not finish[p] and all(need[p][j] <= work[j] for j in range(m)):
                # Process can execute
                work = [work[j] + allocation[p][j] for j in range(m)]
                safe_sequence.append(p)
                finish[p] = True
                found = True
                break
        if not found:
            return None  # No safe sequence possible

    return safe_sequence
