class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        for i in nums:
            if nums.count(i)>2 or nums.count(i)!=1 and nums.count(i)%2!=0:
                return False
        else:
            return True
        