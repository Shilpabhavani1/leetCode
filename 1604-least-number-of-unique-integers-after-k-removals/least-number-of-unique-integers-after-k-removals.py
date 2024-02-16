class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = {}
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        l=[]
        for i,j in d.items():
            l.append((j,i))
        l.sort()
        l1=[]
        for i in l:
            l1.extend([i[1]]*i[0])
        return len(set(l1[k:]))




        # d = sorted(d.items(), key=lambda x:x[1])
        # ans = []
        # for i in d:
        #     ans.append([i[0]]*i[1])
        # # print(ans)
        # r = []
        # for i in ans:
        #     for j in i:
        #         r.append(j)
        # # print(set(r[k:]))
        # return len(set((r[k:])))