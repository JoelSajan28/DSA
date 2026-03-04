from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        best = 0  # starting at 0 counts

        for g in gain:
            altitude += g
            if altitude > best:
                best = altitude

        return best