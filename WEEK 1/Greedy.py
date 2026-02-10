# Problem 1

# Sample Input 
# 1
# 3 50
# 60 10
# 100 20
# 120 30

t = int(input())

for _ in range(t):
    n, W = map(int, input().split())
    items = []

    for _ in range(n):
        v, w = map(int, input().split())
        items.append((v / w, v, w))  # (ratio, value, weight)

    # sort by ratio descending
    items.sort(key=lambda x: x[0], reverse=True)

    total_value = 0.0
    capacity = W

    for ratio, value, weight in items:
        if capacity == 0:
            break

        if weight <= capacity:
            total_value += value
            capacity -= weight
        else:
            total_value += ratio * capacity
            break

    print(f"{total_value:.6f}")


# Output : 240.000000





# Problem 2

"""
Sample Input:
1
5
2 100
1 19
2 27
1 25
3 15

Sample Output:
3 142

Explanation:
1. Sort jobs by profit (descending): 
   (2, 100), (2, 27), (1, 25), (1, 19), (3, 15)
2. Pick (2, 100): Slot 2 is free. Profit = 100.
3. Pick (2, 27): Slot 2 is taken. Find latest free slot < 2. Slot 1 is free. Profit = 100 + 27 = 127.
4. Pick (1, 25): Slot 1 is taken. Slot 0 is invalid. Skip.
5. Pick (1, 19): Slot 1 is taken. Skip.
6. Pick (3, 15): Slot 3 is free. Profit = 127 + 15 = 142.
Total: 3 jobs, 142 profit.
"""

def get_parent(parent, i):
    path = []
    while i != parent[i]:
        path.append(i)
        i = parent[i]
    
    for node in path:
        parent[node] = i
    return i

def solve():
    try:
        line = input().split()
        if not line: return
        t = int(line[0])

        for _ in range(t):
            try:
                line = input().split()
                if not line: break
                n = int(line[0])
            except EOFError:
                break

            jobs = []
            max_deadline = 0

            for _ in range(n):
                d_str, p_str = input().split()
                d = int(d_str)
                p = int(p_str)
                jobs.append((d, p))
                
                if d > max_deadline:
                    max_deadline = d

            
            jobs.sort(key=lambda x: x[1], reverse=True)

            parent = list(range(max_deadline + 1))

            jobs_done = 0
            total_profit = 0

            for d, p in jobs:
                available_slot = get_parent(parent, min(d, max_deadline))
                if available_slot > 0:
                    jobs_done += 1
                    total_profit += p
                    
                    parent[available_slot] = get_parent(parent, available_slot - 1)

            print(f"{jobs_done} {total_profit}")

    except EOFError:
        pass

if __name__ == "__main__":
    solve()
    