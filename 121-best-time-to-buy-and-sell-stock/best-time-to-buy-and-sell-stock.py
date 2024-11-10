class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        buy=prices[0]
        p=0
        for i in range(1,len(prices)):
            if buy>prices[i]:
                buy=prices[i]
            elif prices[i]-buy>p:
                p=prices[i]-buy
        return p




















        # l=len(prices)
        # buy=prices[0]
        # p=0
        # for i in range(1,l):
        #     if prices[i]<buy:
        #         buy=prices[i]
        #     elif prices[i]-buy>p:
        #         p=prices[i]-buy
        # return p






















        # #Two pointers concept
        # l,r=0,1
        # maxprofit = 0
        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         profit = prices[r] - prices[l]
        #         maxprofit=max(maxprofit,profit)
        #     else:
        #         l = r
        #     r = r + 1
        # return maxprofit


        # n=len(prices)
        # buy=prices[0]
        # profit=0
        # for i in range(1,n):
        #     if buy>prices[i]:
        #         buy=prices[i]
        #     elif prices[i]-buy>profit:
        #         profit=prices[i]-buy
        # return profit

        