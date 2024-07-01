class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        c=0
        for i in arr:
            if i%2!=0:
                c=c+1
                if c==3:
                    return True
            else:
                c=0
        return False



























        # n=len(arr)
        # l=[]
        # k=[]
        # for i in range(n):
        #     for j in range(i,n):
        #         a=arr[i:j+1]
        #         # print(a)
        #         l.append(a)
        # # print(l)
        # for i in l:
        #     # print(i)
        #     if len(i)==3:
        #         # print(i)
        #         k.append(i)
        # print(k)
        # return False
        # l=[]
        # for i in range(2,n+1):
        #     s=sum(arr[:i])
        #     # print(s)
        #     l.append(s)
        # print(l)
        # for i in l:
        #     if i%2!=0:
        #         return True
        # return False
        
        