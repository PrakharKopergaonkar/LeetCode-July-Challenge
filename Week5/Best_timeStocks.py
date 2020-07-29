# The solution - using DP
# We have two conditions on a particular day -
# 1. Either we have stock on that day dp[i][1]
# -> We have bought stock on that day dp[i-2][0] - prices[i]
# -> Just Carryforwarding dp[i-1][1]
# 2. We have no stock on that day dp[i][0] 
# -> We sold all that day. dp[i-1][0] + prices[i]
# -> Just carryforwarding dp[i-1][0]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0 for i in range(2)] for j in range(len(prices))]
        if(len(prices)<=1) : return 0
        if(len(prices)==0 and prices[1]>=prices[0]) : return prices[1] - prices[0] 
        if(len(prices)==0 and prices[1]<prices[1]) : return 0
        dp[0][1] = -prices[0]
        dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
        dp[1][1] = max(dp[0][1],dp[0][0] - prices[1])
        for i in range(2,len(dp)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-2][0]-prices[i],dp[i-1][1])
        
        return dp[-1][0]