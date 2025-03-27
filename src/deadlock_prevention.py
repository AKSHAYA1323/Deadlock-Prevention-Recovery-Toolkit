def is_safe(processes, allocation, max_demand, available):
    """
    Banker's Algorithm for Deadlock Prevention.
    Returns a safe sequence if the system is in a safe state.
    """
    work = available[:]
    finish = [False] * len(processes)
    safe_sequence = []

    while len(safe_sequence) < len(processes):
        found = False
        for i, process in enumerate(processes):
            if not finish[i]:
                if all(max_demand[i][j] - allocation[i][j] <= work[j] for j in range(len(available))):
                    work = [work[j] + allocation[i][j] for j in range(len(available))]
                    safe_sequence.append(process)
                    finish[i] = True
                    found = True
                    break

        if not found:
            return False, []  # No safe sequence found

    return True, safe_sequence