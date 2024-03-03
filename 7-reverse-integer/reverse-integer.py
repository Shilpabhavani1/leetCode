class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            a=int(str(x)[::-1])
        else:
            a=-(int(str(abs(x))[::-1]))
        if a <= -2**31 or a >= 2**31-1:
            return 0
        else:
            return a
        

        