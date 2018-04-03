import collections
def leastInterval(tasks, N):
    task_counts = collections.Counter(tasks).values()
    print task_counts
    M = max(task_counts)
    Mct = task_counts.count(M)
    print Mct
    return max(len(tasks), (M - 1) * (N + 1) + Mct)

print leastInterval(["A","A","A","B","B","B","C","D","E","E","E","F"], 2)