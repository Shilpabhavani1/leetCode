class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False



        # for i in nums:
        #     if nums.count(i)>1:
        #         return True
        # return False
        