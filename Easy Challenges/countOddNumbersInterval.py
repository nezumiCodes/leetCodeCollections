import math

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        N = (high - low)//2
        return N+1 if (high%2!=0 or low%2!=0) else N