class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        count = 0
        product = 1
        left = 0
        
        for right, num in enumerate(nums):
            product *= num
            while product >= k:
                product /= nums[left]
                left += 1
            count += right - left + 1
        
        return count



































# import math
# class Solution:
#     def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
#         l=[]
#         m=[]
#         c=0
#         for i in range(len(nums)):
#             for j in range(i,len(nums)):
#                 # print(nums[i:j+1])
#                 a=nums[i:j+1]
#                 # print(a)
#                 l.append(a)
#         # print(l)
#         for i in l:
#             # print(i)
#             p=math.prod(i)
#             # print(p)
#             m.append(p)
#         # print(m)
#         for i in m:
#             if i<k:
#                 c=c+1
#         return c
        