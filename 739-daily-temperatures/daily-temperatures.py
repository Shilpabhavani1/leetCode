class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        s=[]
        n=len(t)
        ans=[0]*n
        for i in range(n-1,-1,-1):
            while(s!=[] and t[s[-1]]<=t[i]):
                s.pop()
            if(s!=[] and t[s[-1]]>t[i]):
                ans[i]=s[-1]-i
            else:
                ans[i]=0
            s.append(i)
        return ans
        