class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p=[]
        n=[]
        for i in nums:
            if i>0:
                p.append(i)
            if i<0:
                n.append(i)
        r=[]
        for i in range(len(p)):
            r.append(p[i])
            r.append(n[i])
        return r
            
        