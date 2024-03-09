class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # l=[]
        # for i in nums1:
        #     if i in nums2:
        #         l.append(i)
        # return l[0]
        set_nums2 = set(nums2)
        for num in nums1:
            if num in set_nums2:
                return num
        return -1