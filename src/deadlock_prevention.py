def is_safe(processes, available, max_demand, allocation):
    """
    Implements Banker's Algorithm for Deadlock Prevention.
    """
    num_processes = len(processes)
    num_resources = len(available)
    work = available[:]
    finish = [False] * num_processes
    safe_sequence = []

    while len(safe_sequence) < num_processes:
        found = False
        for i in range(num_processes):
            if not finish[i] and all(max_demand[i][j] - allocation[i][j] <= work[j] for j in range(num_resources)):
                work = [work[j] + allocation[i][j] for j in range(num_resources)]
                finish[i] = True
                safe_sequence.append(processes[i])
                found = True
                break

        if not found:
            return False, []

    return True, safe_sequence
