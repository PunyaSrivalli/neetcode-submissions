class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curmax, curmin = 1, 1
        for i in nums:
            temp = curmax
            curmax = max(i, i*curmax, i*curmin)
            curmin = min(i, i*temp, i*curmin)
            res = max(res, curmax)
        return res