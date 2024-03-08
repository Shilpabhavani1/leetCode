class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        v=d.values()
        # print(v)
        maxi=max(v)
        l=[]
        for i in v:
            if i==maxi:
                l.append(i)
                # print(l)
        return sum(l)