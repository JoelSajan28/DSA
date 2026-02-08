# You are given a sorted array and then you are asked to remove duplicates

def remove_sorted_array_duplicates(arr):
    if not arr:
        return []
    
    write = 1
    
    for read in range(1, len(arr)):
        if arr[read] !=  arr[write - 1]:
            arr[write] = arr[read]
            write += 1
    return write

nums = [1,1,1,1,2,2,3,4,4,5]
remove_sorted_array_duplicates(nums)
print(nums)

def move_zeroes(nums):
    write = 0
    for x in nums:
        if x != 0:
            nums[write] = x
            write += 1

    for i in range(write, len(nums)):
        nums[i] = 0


def max_profit(prices):
    min_price = float("inf")
    best = 0

    for p in prices:
        min_price = min(min_price, p)
        best = max(best, p - min_price)

    return best


def product_except_self(nums):
    n = len(nums)
    ans = [1] * n

    left = 1
    for i in range(n):
        ans[i] = left
        left *= nums[i]

    right = 1
    for i in range(n - 1, -1, -1):
        ans[i] *= right
        right *= nums[i]

    return ans


def subarray_sum(nums, k):
    freq = {0: 1}   # prefix_sum -> count
    prefix = 0
    count = 0

    for x in nums:
        prefix += x
        count += freq.get(prefix - k, 0)
        freq[prefix] = freq.get(prefix, 0) + 1

    return count


def three_sum(nums):
    nums.sort()
    res = []
    n = len(nums)

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        if nums[i] > 0:
            break

        l, r = i + 1, n - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1

    return res


def longest_consecutive(nums):
    s = set(nums)
    best = 0

    for x in s:
        if x - 1 not in s:  # start
            y = x
            while y in s:
                y += 1
            best = max(best, y - x)

    return best


def trap(height):
    l, r = 0, len(height) - 1
    left_max = right_max = 0
    water = 0

    while l < r:
        if height[l] <= height[r]:
            if height[l] >= left_max:
                left_max = height[l]
            else:
                water += left_max - height[l]
            l += 1
        else:
            if height[r] >= right_max:
                right_max = height[r]
            else:
                water += right_max - height[r]
            r -= 1

    return water


def min_subarray_len(target, nums):
    left = 0
    curr = 0
    best = float("inf")

    for right, x in enumerate(nums):
        curr += x
        while curr >= target:
            best = min(best, right - left + 1)
            curr -= nums[left]
            left += 1

    return 0 if best == float("inf") else best


def max_subarray(nums):
    best = nums[0]
    curr = nums[0]

    for x in nums[1:]:
        curr = max(x, curr + x)
        best = max(best, curr)

    return best
