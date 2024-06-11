class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        l=[]
        for i in arr2:
            while i in arr1:
                l.append(i)
                arr1.remove(i)
        return l+sorted(arr1)

        # l=[]
        # for i in arr2:
        #     l.append(i)
        # # print(l)
        # arr1.sort()
        # for i in arr1:
        #     if i not in arr2:
        #         l.append(i)
        # # print(l)
        # return l
        