class Solution:
    def makeFancyString(self, s: str) -> str:
        l=""
        for i in s:
            if l[-2:]!=i+i:
                l+=i
        # print(l)
        return l

        