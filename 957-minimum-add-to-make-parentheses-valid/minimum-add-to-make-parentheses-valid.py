class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        while "()" in s:
            s= s.replace("()","",1)
        return len(s)
        