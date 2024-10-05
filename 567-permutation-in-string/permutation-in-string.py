class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1=len(s1)
        n2=len(s2)
        c1=Counter(s1)
        c2=Counter(s2[:n1])
        for i in range(n1,n2):
            if c1==c2:
                return True
            c2[s2[i-n1]]-=1
            c2[s2[i]]+=1
        return c1==c2
        