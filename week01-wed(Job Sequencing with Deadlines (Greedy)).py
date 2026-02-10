# 1
# 5
# 2 100
# 1 19
# 2 27
# 1 25
# 3 15
# output 3 142

def job_sequencing(jobs, n):
    # Sort jobs by profit (descending)
    jobs.sort(key=lambda x: x[1], reverse=True)

    # Find maximum deadline
    max_deadline = max(job[0] for job in jobs)

    # Time slots (False = free, True = occupied)
    slots = [False] * (max_deadline + 1)

    jobs_done = 0
    total_profit = 0

    for deadline, profit in jobs:
        # Try to schedule job at latest available slot
        for t in range(deadline, 0, -1):
            if not slots[t]:
                slots[t] = True
                jobs_done += 1
                total_profit += profit
                break

    return jobs_done, total_profit


# Driver code
T = int(input())
for _ in range(T):
    N = int(input())
    jobs = []

    for _ in range(N):
        D, P = map(int, input().split())
        jobs.append((D, P))

    count, profit = job_sequencing(jobs, N)
    print(count, profit)
