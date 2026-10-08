class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        max_cur, min_cur = 1, 1
        for n in nums:
            if n == 0:
                max_cur, min_cur  = 1,1
                continue
            temp = max_cur*n
            max_cur = max(max_cur*n,min_cur*n,n)
            min_cur = min(temp, min_cur*n,n)

            res = max(max_cur, res)
        return res