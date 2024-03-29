class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx,ans,l,r,n=max(nums),0,0,0,len(nums)
        while r<n:
            k-= nums[r]==mx
            r+=1
            while k==0:
                k+=nums[l]==mx
                l+=1
            ans+=l
        return ans;




















# class Solution:
#     def countSubarrays(self, nums: List[int], k: int) -> int:
#         # print(max(nums))
#         m=max(nums)
#         c=0
#         l=[]
#         if nums.count(m)<k:
#             return 0
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 # print(nums[i:j+1])
#                 a=nums[i:j+1]
#                 l.append(a)
#         for i in l:
#             # print(i)
#             if i.count(m)>=k:
#                 # print(i)
#                 c=c+1
#         return c
        