from scheduler import Scheduler

class PreemptivePS(Scheduler):
    def gantt_chart(self):
        sorted_processes = sorted(self.processes, key=lambda process: process.priority)

        gantt = {}
        burst_time_track = {process:process.burst_time for process in sorted_processes}
        
        executed_time = 0
        executed_process = None

        last_occurence = 0
        while len(sorted_processes) > 0:
            for process in sorted_processes:
                if executed_process is process:
                    break
                elif executed_time < process.arrival_time:
                    continue
                
                if executed_process is not None:
                    gantt[last_occurence] = (executed_process, last_occurence + (executed_time - last_occurence))

                executed_process = process
                last_occurence = executed_time

                break

            executed_time += 1

            if executed_process is None:
                continue

            burst_time_track[executed_process] -= 1

            if burst_time_track[executed_process] == 0:
                sorted_processes.remove(executed_process)

                gantt[last_occurence] = (executed_process, last_occurence + (executed_time - last_occurence))

                executed_process = None

        return gantt

    def mean_execution_time(self, gantt):
        avg = 0

        for process in self.processes:
            last_executed = None
            time_executed = 0

            for time in reversed(list(gantt.keys())):
                process_data = gantt[time]

                if process is not process_data[0]:
                    continue

                if last_executed is None:
                    last_executed = time
                else:
                    time_executed += (process_data[1] - time)

            avg += last_executed - time_executed - process.arrival_time

        return avg / len(self.processes)