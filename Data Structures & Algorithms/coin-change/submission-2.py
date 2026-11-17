class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def rec(a):
            if a == 0:
                return 0
            if a in memo:
                return memo[a]
            res = 1e9
            for c in coins:
                if a-c >= 0:
                    res = min(res, 1+rec(a-c))
            memo[a] = res
            return res
        return -1 if rec(amount) >= 1e9 else rec(amount)