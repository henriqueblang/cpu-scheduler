import operator

from modules.scheduler.scheduler import Scheduler

class FCFS(Scheduler):
    def gantt_chart(self):
        sorted_processes = sorted(self.processes, key=lambda process: process.arrival_time)
        
        gantt = {}
        remaining_time = sum(process.burst_time for process in sorted_processes)

        last_occurence = 0
        while remaining_time > 0:
            process = sorted_processes[0]

            if last_occurence < process.arrival_time:
                last_occurence += 1
                remaining_time -= 1

                continue

            gantt[last_occurence] = (process, last_occurence + process.burst_time)

            last_occurence += process.burst_time 
            remaining_time -= process.burst_time

            sorted_processes.remove(process)

        return gantt

    def mean_execution_time(self, gantt):
        return sum((occurence_time - process_data[0].arrival_time) for occurence_time, process_data in gantt.items()) / len(gantt)