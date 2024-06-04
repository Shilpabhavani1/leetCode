class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap={} #hash map val:ind
        for i,n in enumerate(nums):
            diff=target-n
            if diff in prevmap:
                return prevmap[diff],i
            prevmap[n]=i
        return
        # for i in range(len(nums)+1):
        #     if nums[i]+nums[i+1]==target:
        #         return i,i+1
        