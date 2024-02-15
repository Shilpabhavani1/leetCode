class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        for i in range(n-1,-1,-1):
            if sum(nums[:i])>nums[i]:
                return sum(nums[:i+1])
        return -1
        