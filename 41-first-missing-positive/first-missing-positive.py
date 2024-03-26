class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        r=[0 for i in range(n+1)]
        for i in range(n):
            if nums[i]<=0 or nums[i]>n+1:
                continue
            r[nums[i]-1]=i+1
        for j in range(n+1):
            if r[j]==0:
                return j+1
        return -1

        