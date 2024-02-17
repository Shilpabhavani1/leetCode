class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    l.append(i)
                    l.append(j)
        return l














        # for i in range(len(nums)-1):
        #     if nums[i]+nums[i+1]==target:
        #         return (i,i+1)
        # return []
        # l=[]
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             l.append(i)
        #             l.append(j)
        #             break
        # return l
        