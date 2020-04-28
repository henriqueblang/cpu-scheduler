from abc import ABC, abstractmethod

class Scheduler(ABC):
    def __init__(self, processes):
        self.processes = processes

    def print_gantt_chart(self, gantt):
        pr_str = ""
        chart_str = ""
        timeline_str = ""
        auxiliar_spaces = 0

        last_occurence = 0
        for occurence_time, process_data in gantt.items():
            process, finish_time = process_data

            if last_occurence != occurence_time:
                time_difference = occurence_time - last_occurence

                auxiliar_spaces = (2 * time_difference) - 1

                occurence_time_digits = len(str(occurence_time))

                pr_str += " " * (auxiliar_spaces + 2)
                chart_str += "|" + ("--" * time_difference)
                timeline_str += str(last_occurence) + (" " * ((auxiliar_spaces + 1) - (occurence_time_digits - 1)))

            time_difference = finish_time - occurence_time

            auxiliar_spaces = (2 * time_difference) - 1

            process_id_digits = len(str(process.id))
            occurence_time_digits = len(str(occurence_time))

            pr_str += "P" + str(process.id) + (" " * (auxiliar_spaces - (process_id_digits - 1)))
            chart_str += "|" + ("--" * time_difference)
            timeline_str += str(occurence_time) + (" " * ((auxiliar_spaces + 1) - (occurence_time_digits - 1)))

            last_occurence = finish_time

        timeline_str += str(last_occurence)

        print(pr_str)
        print(chart_str)
        print(timeline_str)
            
    @abstractmethod
    def gantt_chart(self):
        pass

    @abstractmethod
    def mean_execution_time(self):
        pass