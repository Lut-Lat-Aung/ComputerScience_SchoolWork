def round_robin(processes, quantum):
    n = len(processes)
    waiting_time = [0] * n
    remaining_burst_time = [process[1] for process in processes]

    time = 0
    while any(remaining_burst_time):
        for i in range(n):
            if remaining_burst_time[i] > 0:
                if remaining_burst_time[i] > quantum:
                    time += quantum
                    remaining_burst_time[i] -= quantum
                else:
                    time += remaining_burst_time[i]
                    waiting_time[i] = time - processes[i][1]
                    remaining_burst_time[i] = 0

    print("Process\tBurst Time\tWaiting Time")
    total_waiting_time = 0
    for i in range(n):
        total_waiting_time += waiting_time[i]
        print(f"{processes[i][0]}\t\t{processes[i][1]}\t\t{waiting_time[i]}")

    average_waiting_time = total_waiting_time / n
    print(f"\nAverage Waiting Time: {average_waiting_time}")

# Example usage:
processes = [(1, 14), (2, 8), (3, 6), (4, 4)]
quantum = 4
round_robin(processes, quantum)
