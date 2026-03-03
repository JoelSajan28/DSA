"""
Key rule

You can plant at index i if:

flowerbed[i] == 0

left is empty or i == 0

right is empty or i == n-1

When you plant, set flowerbed[i] = 1 to avoid double-counting.

Time: O(n)
Space: O(1)
"""
from typing import List

def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    if n == 0:
        return True

    L = len(flowerbed)

    for i in range(L):
        if flowerbed[i] == 0:
            left_empty = (i == 0) or (flowerbed[i - 1] == 0)
            right_empty = (i == L - 1) or (flowerbed[i + 1] == 0)

            if left_empty and right_empty:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True

    return False