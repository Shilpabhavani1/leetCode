class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle_time = 2 * n - 2
        t = time % cycle_time
    
        if t < n:
            return t + 1
        else:
            return n - (t - n + 1)