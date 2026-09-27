class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        
        def dp(a):
            res = 1e9
            if a == 0:
                return 0
            if a in memo:
                return memo[a]
            for c in coins:
                if a - c >= 0:
                    res = min(res, 1+dp(a-c))
            memo[a] = res
            return res
        return dp(amount) if dp(amount) != 1e9 else -1