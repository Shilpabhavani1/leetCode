from typing import List
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        l=[]
        k=[]
        if n == 1:return 1
        for i in trust:
            l.append(i[0])
            k.append(i[1])
        for i in k:
            if i not in l and k.count(i)>=n-1:
                return i
        return -1
        # d = {}
        # l = []
        # if n == 1 and len(trust) == 0:return 1
        # for i in trust:
        #     l.append(i[0])
        #     if i[1] not in d:
        #         d[i[1]] = 1
        #     else:
        #         d[i[1]] += 1
        # # print(d,l)
        # for i in d:
        #     if i in l:
        #         return -1
        #     return i
        # return -1
        