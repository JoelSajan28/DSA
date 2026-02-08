

def max_subarray(arr):
    current_sum = arr[0]
    max_sum = 0
    
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(current_sum, max_sum)

    
    return max_sum
