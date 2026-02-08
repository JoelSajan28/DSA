# TC: O(N)
# SC: O(N)

def two_sum(arr, target):
    seen = {}
    lst = []
    for index, num in enumerate(arr):
        check = target - num
        if check in seen:
            lst.append([seen[check], index])
        
        seen[num] = index
    return lst 

print(two_sum([1,2,3,4,5,6], 6))


