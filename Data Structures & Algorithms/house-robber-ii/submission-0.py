class Solution:
    def rob(self, nums: List[int]) -> int:
        nums1 = nums[1:]
        nums2 = nums[:-1]
        rob1, rob2 = 0,0
        for i in range(len(nums1)):
            temp = max(rob1 + nums1[i], rob2)
            rob1 = rob2
            rob2 = temp
        nums1_max = rob2
        rob1, rob2 = 0,0
        for i in range(len(nums2)):
            temp = max(rob1 + nums2[i], rob2)
            rob1 = rob2
            rob2 = temp
        nums2_max = rob2
        return max(nums[0],nums1_max, nums2_max)