class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    def helper(self, arr):
        rob1, rob2 = 0, 0
        for i in range(len(arr)):
            temp = max(arr[i]+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2