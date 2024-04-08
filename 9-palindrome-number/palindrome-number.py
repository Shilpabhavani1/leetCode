class Solution:
    def isPalindrome(self, x: int) -> bool:

        s=str(x)
        if s==s[::-1]:
            return True
        return False














        # if x<0:
        #     return False
        # n=x
        # r=0
        # while n:
        #     r=r*10+n%10
        #     n=n//10
        # return r == x
        