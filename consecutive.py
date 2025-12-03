def longest_consecutive(arr):
    if not arr:
        return 0
    arr = sorted(arr)
    max_len = 1
    curr_len = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            continue
        if arr[i] == arr[i-1] + 1:
            curr_len += 1
        else:
            curr_len = 1  
        max_len = max(max_len, curr_len)
    return max_len
print(longest_consecutive([1, 9, 3, 10, 4, 20, 2]))
