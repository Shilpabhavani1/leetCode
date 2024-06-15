class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ma=-99999
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            if ma<sum:
                ma=sum
            if sum<0:
                sum=0
        return ma











        # l=[]
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         a=nums[i:j+1]
        #         # print(a)
        #         l.append(sum(a))
        # return max(l)



















        # maxSum = float('-inf')
        # currentSum = 0
        
        # for num in nums:
        #     currentSum += num
            
        #     if currentSum > maxSum:
        #         maxSum = currentSum
            
        #     if currentSum < 0:
        #         currentSum = 0
        
        # return maxSum