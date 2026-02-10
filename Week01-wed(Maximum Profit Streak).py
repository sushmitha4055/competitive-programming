def max_crossing_sum(arr, left, mid, right):
    # Maximum suffix sum on left side
    total = 0
    left_max = float('-inf')
    for i in range(mid, left - 1, -1):
        total += arr[i]
        left_max = max(left_max, total)

    # Maximum prefix sum on right side
    total = 0
    right_max = float('-inf')
    for i in range(mid + 1, right + 1):
        total += arr[i]
        right_max = max(right_max, total)

    return left_max + right_max


def max_subarray_sum(arr, left, right):
    # Base case: only one element
    if left == right:
        return arr[left]

    mid = (left + right) // 2

    left_sum = max_subarray_sum(arr, left, mid)
    right_sum = max_subarray_sum(arr, mid + 1, right)
    cross_sum = max_crossing_sum(arr, left, mid, right)

    return max(left_sum, right_sum, cross_sum)


# Driver code
T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    print(max_subarray_sum(arr, 0, N - 1))
