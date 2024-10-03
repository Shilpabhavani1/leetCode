from collections import defaultdict
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        tar_residual = sum(nums)%p
        if tar_residual == 0:
            return 0
        
        # now find the smallest subarray which satisfies:
        # sum(subarray)%p = tar_residual
        prefix_sum, ret = 0, len(nums)
        residual2lastIdx = defaultdict(int)
        residual2lastIdx[0] = -1
        
        for i, num in enumerate(nums):
            prefix_sum += num
            cur_residual = prefix_sum%p
            d = (cur_residual-tar_residual)%p
            if d in residual2lastIdx:
                ret = min(ret, i-residual2lastIdx[d])
            residual2lastIdx[cur_residual] = i
           
        return ret if ret < len(nums) else -1
            

# class Solution:
#     def minSubarray(self, nums: List[int], p: int) -> int:
#         c=0
#         l=[]
#         for i in range(len(nums)):
#             for j in range(i,len(nums)):
#                 a=nums[i:j+1]
#                 # print(a)
#                 l.append(a)
#         # print(l)
#         for i in l:
#             print(sum(i))
#             if sum(i)%p==0:
#                 c+= len(nums)-len(i)
#         return c