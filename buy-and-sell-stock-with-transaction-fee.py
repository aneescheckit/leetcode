class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # 0 if purchased
        # 1 if sold

        dp = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            if buying:
                buy = dfs(i+1, False) - prices[i]
                not_buy = dfs(i+1, buying)
                dp[(i, buying)] = max(buy, not_buy)
            else:
                sell = dfs(i+1, True) + prices[i] - fee
                not_sell = dfs(i+1, buying)
                dp[(i, buying)] = max(sell, not_sell)
            return dp[(i, buying)]
        return dfs(0, True)