def detect_deadlock(processes, allocation, available, request):
    """
    Detects deadlock using Resource Allocation Graph (RAG).
    Returns a list of deadlocked processes.
    """
    work = available[:]
    finish = {p: False for p in processes}
    
    while True:
        progress = False
        for p in processes:
            if not finish[p] and all(request[p][j] <= work[j] for j in range(len(work))):
                work = [work[j] + allocation[p][j] for j in range(len(work))]
                finish[p] = True
                progress = True
                break
        if not progress:
            break

    deadlocked = [p for p in processes if not finish[p]]
    return deadlocked if deadlocked else None
