def detect_deadlock(processes, resources, allocation, request):
    """
    Detects deadlocks using Wait-for Graph Algorithm.
    """
    num_processes = len(processes)
    work = [resources[i] - sum(allocation[j][i] for j in range(num_processes)) for i in range(len(resources))]
    finish = [False] * num_processes
    deadlocked = []

    while True:
        found = False
        for i in range(num_processes):
            if not finish[i] and all(request[i][j] <= work[j] for j in range(len(resources))):
                work = [work[j] + allocation[i][j] for j in range(len(resources))]
                finish[i] = True
                found = True

        if not found:
            break

    for i in range(num_processes):
        if not finish[i]:
            deadlocked.append(processes[i])

    return deadlocked
