class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d={}
        r=[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        # print(d)
        s = dict(sorted(d.items(), key=lambda item: (item[1],-item[0])))
        # print(s)
        for i,j in s.items():
            for k in range(j):
                r.append(i)
        return r