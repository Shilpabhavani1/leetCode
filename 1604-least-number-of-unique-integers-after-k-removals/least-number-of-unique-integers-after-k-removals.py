class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = {}
        for i in arr:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        freq = sorted(freq.items(), key=lambda x:x[1])
        ans = []
        for i in freq:
            ans.append([i[0]]*i[1])
        # print(ans)
        secans = []
        for i in ans:
            for j in i:
                secans.append(j)
        # print(set(secans[k:]))
        return len(set((secans[k:])))