class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        x = a = 0
        for i in range(len(nums)):
            if nums[i]>0:
                x = nums[i]
                a = i
                break
        print(nums,a,x)
        if x==1:
            for i in range(a+1,len(nums)):
                if nums[i]!=nums[i-1]+1:return nums[i-1]+1
            else:return nums[-1]+1
        return 1
































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

        