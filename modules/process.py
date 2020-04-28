g_id = 0

class Process:
    def __init__(self, burst_time, arrival_time = 0, priority = 0):
        global g_id

        self.id = g_id
        g_id += 1

        self.priority = priority
        self.burst_time = burst_time
        self.arrival_time = arrival_time