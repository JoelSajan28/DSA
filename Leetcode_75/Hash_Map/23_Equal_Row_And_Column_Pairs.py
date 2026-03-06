from typing import List
from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)

        row_count = Counter(tuple(row) for row in grid)

        ans = 0
        for c in range(n):
            col = tuple(grid[r][c] for r in range(n))
            ans += row_count[col]

        return ans