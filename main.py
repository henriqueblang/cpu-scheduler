from process import Process
from fcfs import FCFS
from ps import PreemptivePS

p1 = Process(4, arrival_time=2, priority=1)
p2 = Process(1, arrival_time=6, priority=2)
p3 = Process(7, arrival_time=0, priority=4)
p4 = Process(5, arrival_time=1, priority=3)
p5 = Process(6, arrival_time=3, priority=7)
p6 = Process(2, arrival_time=8, priority=5)

l = [p1, p2, p3, p4, p5, p6]
fcfs = FCFS(l)
pps = PreemptivePS(l)

g1 = pps.gantt_chart()
g2 = fcfs.gantt_chart()


print("PPS")
pps.print_gantt_chart(g1)
print(f"{pps.mean_execution_time(g1)} ms")
print("FCFS")
fcfs.print_gantt_chart(g2)
print(f"{fcfs.mean_execution_time(g2)} ms")