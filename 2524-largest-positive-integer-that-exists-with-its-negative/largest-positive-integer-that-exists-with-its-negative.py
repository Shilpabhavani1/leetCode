# class Solution:
#     def findMaxK(self, nums: List[int]) -> int:
#         l=[]
#         k=[]
#         for i in nums:
#             if i>=0:
#                 l.append(i)
#             else:
#                 k.append(i)
#         a=max(k)
#         if abs(a) in k:
#             return a
#         return -1

        
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        Set = set(nums) ### convert nums into a set
        maxSoFar = -inf
        res = -inf
        for n in nums:
        	### check condition 1-3
            if n>0 and -n in Set and n>maxSoFar:
                maxSoFar = n
                res = n
        ### If there is no such integer (res==-inf which never got updated), return -1.
        return res if res!=-inf else -1