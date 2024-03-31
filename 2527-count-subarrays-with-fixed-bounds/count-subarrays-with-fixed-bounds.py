class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        start = 0
        min_idx, max_idx = 0,0
        min_found, max_found = False, False
        ans = 0

        for idx,num in enumerate(nums):
            if num == minK:
                min_found = True
                min_idx = idx
            if num == maxK:
                max_found = True
                max_idx = idx
            if num < minK or num > maxK:
                min_found = max_found = False
                start = idx + 1
            elif min_found and max_found:
                ans += min(min_idx, max_idx) - start + 1
            
        return ans























# class Solution:
#     def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
#         l=[]
#         c=0
#         for i in range(len(nums)):
#             for j in range(i,len(nums)):
#                 a=nums[i:j+1]
#                 l.append(a)
#         # print(l)
#         for i in l:
#             # print(i)
#             if min(i) == minK and max(i) == maxK:
#                 c=c+1

#         return c
        