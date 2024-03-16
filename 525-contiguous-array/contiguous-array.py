# class Solution:
#     def findMaxLength(self, nums: List[int]) -> int:
#         l=[]
#         for i in range(len(nums)):
#             for j in range(i,len(nums)):
#                 # print(nums[i:j+1])
#                 a=nums[i:j+1]
#                 l.append(a)
#         # print(l)
#         m = 0
#         for i in l:
#             # print(l[i])
#             # print(i)
#             if i.count(0) == i.count(1):
#                 m = max(m,len(i))
#         return m
        
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {}
        sum_val = 0
        max_len = 0
        for i, num in enumerate(nums):
            sum_val += 1 if num == 1 else -1
            if sum_val == 0:
                max_len = i + 1
            elif sum_val in mp:
                max_len = max(max_len, i - mp[sum_val])
            else:
                mp[sum_val] = i
        return max_len