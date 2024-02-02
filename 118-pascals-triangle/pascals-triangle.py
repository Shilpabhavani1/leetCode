class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        mod=10**9+7
        l=[[1],[1,1]]
        for i in range(1,numRows-1):
            lst=[1,1]
            l1=l[i]
            for j in range(1,i+1):
                lst.insert(j,l1[j]+l1[j-1]%mod)
            l.append(lst)
        return l


        