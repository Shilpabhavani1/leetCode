class Solution:
    def maxDepth(self, s):
        count = 0
        n = 0
        for i in s:
            if i == "(":
                count += 1
                if n < count:
                    n = count
            if i == ")":
                count -= 1
        return(n)