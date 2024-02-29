class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            if c<1 or i>nums[c-1]:
                nums[c]=i
                c=c+1
        return c
        