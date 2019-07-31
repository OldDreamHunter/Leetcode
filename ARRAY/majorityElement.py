"""
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在众数。
"""
class Solution(object):
    def majorityElement(self, nums):
        if len(nums) == 0: return None
        if len(nums) == 1: return nums[0]
        stack = []
        for eachnum in nums:
            if stack == []:
                stack.append(eachnum)
            elif eachnum == stack[-1]:
                stack.append(eachnum)
            elif eachnum != stack[-1]:
                stack.pop()
        return stack[-1]




