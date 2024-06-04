class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        buy=prices[0]
        profit=0
        for i in range(1,n):
            if buy>prices[i]:
                buy=prices[i]
            elif prices[i]-buy>profit:
                profit=prices[i]-buy
        return profit

        