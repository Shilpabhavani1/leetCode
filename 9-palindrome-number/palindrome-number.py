class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        n=x
        r=0
        while n:
            r=r*10+n%10
            n=n//10
        return r == x
        