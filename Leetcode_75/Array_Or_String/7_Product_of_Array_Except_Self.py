def product_of_array(arr):
    n = len(arr)
    new_arr = [1]*n

    left = 1

    for index in range(n):
        new_arr[index] = left
        left *= arr[index] 
    
    print(new_arr)

    right = 1

    for index in range(n-1, -1, -1):
        new_arr[index] *= right
        right *= arr[index]
        
    
    print(new_arr)


product_of_array([1,2,3,4])