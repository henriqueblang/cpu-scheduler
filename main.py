from tabulate import tabulate

from modules.process import Process
from modules.scheduler.fcfs import FCFS
from modules.scheduler.ps import PreemptivePS

if __name__ == "__main__":
    processes = []

    user_input = True
    while user_input:
        print("\nNew process input...")

        arrival_time = input("\tProcess arrival time: ")
        priority     = input("\tProcess priority: ")
        burst_time   = input("\tProcess burst time: ")

        try:
            arrival_time = int(arrival_time)
            priority     = int(priority)
            burst_time   = int(burst_time)
        except:
            print("Invalid input...\n")

            continue

        new_process = Process(burst_time, arrival_time, priority)

        processes.append(new_process)
        print(f"New process [id: {new_process.id}] added successfully.")
        
        user_input = input("Keep adding processes? [y/n] ") == "y"

    print("\n" + tabulate(
        [[process.id, process.arrival_time, process.priority, process.burst_time] for process in processes],
        headers=["Process", "Arrival Time", "Priority", "Burst Time"]))

    print("\nRunning scheduling algorithms...\n")
    
    print("> First Come First Served")

    fcfs = FCFS(processes)
    gantt = fcfs.gantt_chart()

    print("\tGantt Chart:")
    fcfs.print_gantt_chart(gantt)
    print(f"\tMean execution time: {fcfs.mean_execution_time(gantt):.2f} ms\n")

    print("> Preemptive Priority Scheduling")

    pps = PreemptivePS(processes)
    gantt = pps.gantt_chart()

    print("\tGantt Chart:")
    pps.print_gantt_chart(gantt)
    print(f"\tMean execution time: {pps.mean_execution_time(gantt):.2f} ms\n")

    print("Finished scheduling algorithms...")