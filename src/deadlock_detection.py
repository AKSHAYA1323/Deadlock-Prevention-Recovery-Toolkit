def detect_deadlock(processes, allocation, max_demand, available):
    """
    Detects deadlock using Resource Allocation Graph.
    Returns a list of deadlocked processes if deadlock exists.
    """
    work = available[:]
    finish = [False] * len(processes)

    for _ in range(len(processes)):
        for i, process in enumerate(processes):
            if not finish[i]:
                if all(max_demand[i][j] - allocation[i][j] <= work[j] for j in range(len(available))):
                    work = [work[j] + allocation[i][j] for j in range(len(available))]
                    finish[i] = True

    deadlocked_processes = [processes[i] for i in range(len(processes)) if not finish[i]]

    return deadlocked_processes
