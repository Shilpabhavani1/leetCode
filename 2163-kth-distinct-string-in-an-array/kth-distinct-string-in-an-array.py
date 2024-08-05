class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        l=[]
        for i in arr:
            if arr.count(i)==1:
                l.append(i)
        print(l)
        for i in range(len(l)):
            if i==k-1:
                return l[i]
        return ""
        