class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l=[0]*len(nums)
        for i in nums:
            if l[i]==0:
                l[i]=1
            elif l[i]==1:
                return i

                

        