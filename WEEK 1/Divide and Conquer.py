# Problem 1

"""
Sample Input:
1
7
4 1 6 2 5 3 2

Expected Output:
1 2 2 3 4 5 6
"""

def merge(left_half, right_half):
    sorted_arr = []
    i = 0
    j = 0
    
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            sorted_arr.append(left_half[i])
            i += 1
        else:
            sorted_arr.append(right_half[j])
            j += 1
    
    
    sorted_arr.extend(left_half[i:])
    sorted_arr.extend(right_half[j:])
    
    return sorted_arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    return merge(left_sorted, right_sorted)

def solve():
    try:

        input_line = input().strip()
        if not input_line:
            return
        t = int(input_line)
        
        for _ in range(t):
            
            try:
                n = int(input().strip())
            except EOFError:
                break
                
            arr = list(map(int, input().strip().split()))
            
            result = merge_sort(arr)
            
            print(*result)
            
    except EOFError:
        pass

if __name__ == "__main__":
    solve()

# Problem 2

"""
Sample Input:
1
9
-2 1 -3 4 -1 2 1 -5 4

Expected Output:
6
"""

def max_crossing_sum(arr, low, mid, high):
    left_sum = -10**18  
    current_sum = 0
    for i in range(mid, low - 1, -1):
        current_sum += arr[i]
        if current_sum > left_sum:
            left_sum = current_sum
            
    # Include elements on right of mid
    right_sum = -10**18
    current_sum = 0
    for i in range(mid + 1, high + 1):
        current_sum += arr[i]
        if current_sum > right_sum:
            right_sum = current_sum
            
    return left_sum + right_sum

def max_subarray_sum(arr, low, high):
    if low == high:
        return arr[low]
    
    # Divide
    mid = (low + high) // 2
    
    left_max = max_subarray_sum(arr, low, mid)
    right_max = max_subarray_sum(arr, mid + 1, high)
    
    crossing_max = max_crossing_sum(arr, low, mid, high)
    
    return max(left_max, right_max, crossing_max)

def solve():
    try:
        input_line = input().strip()
        if not input_line: return
        t = int(input_line)
        
        for _ in range(t):
            try:
                n = int(input().strip())
                arr = list(map(int, input().strip().split()))
                
                print(max_subarray_sum(arr, 0, n - 1))
            except (EOFError, ValueError):
                break
                
    except (EOFError, ValueError):
        pass

if __name__ == "__main__":
    solve()