class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        m=""
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        k=dict(sorted(d.items(),key=lambda item:item[1],reverse=True))
        for i in k:
            m+=(i*d[i])
        return m
            
        