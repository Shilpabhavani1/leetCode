class Solution:
    def majorityElement(self, l: List[int]) -> int:
        l.sort()
        n=len(l)
        return l[n//2]
        # d={}
        # m=[]
        # l=sorted(l)
        # for i in l:
        #     if i not in d:
        #         d[i]=1
        #     else:
        #         d[i]+=1
        # print(d)
        # for i,j in sorted(d.values()):
        #     print(j)
        #     m.append(j)
        # # print(m)

        
            
        