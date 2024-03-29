"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
"""
class Solution(object):
    def singleNumber(self, nums):
        if len(nums) == 1: return nums[0]
        if len(nums) == 0: return 0
        xorresult = nums[0]
        for eachnum in nums[1:]:
            xorresult = xorresult ^ eachnum
        return xorresult

