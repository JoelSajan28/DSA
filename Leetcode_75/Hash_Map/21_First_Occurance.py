from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)                # value -> count
        counts = freq.values()             # all counts
        return len(set(counts)) == len(freq)