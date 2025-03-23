def is_safe_state(processes, available, max_demand, allocation):
    n = len(processes)  # Number of processes
    m = len(available)  # Number of resource types
    
    # Compute Need matrix
    need = [[max_demand[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]
    
    finished = [False] * n
    safe_sequence = []
    work = available[:]

    print("\n🔹 Checking for a Safe State...")
    print(f"Available Resources: {available}")
    print(f"Maximum Demand: {max_demand}")
    print(f"Current Allocation: {allocation}")
    print(f"Need Matrix: {need}")

    for _ in range(n):
        process_found = False
        for i in range(n):
            if not finished[i] and all(need[i][j] <= work[j] for j in range(m)):
                print(f"✅ Process {processes[i]} can execute safely.")

                work = [work[j] + allocation[i][j] for j in range(m)]
                safe_sequence.append(processes[i])
                finished[i] = True
                process_found = True
                break
        
        if not process_found:
            print("❌ No Safe Sequence Found. Deadlock Prevention Failed.")
            return False, []

    print(f"✅ Safe Sequence Found: {safe_sequence}")
    return True, safe_sequence
