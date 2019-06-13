"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

# 我先告诉后面的人我的匹配数是什么，你如果是的，我们就配对
"""

class solution(object):
    def twosum(self,calcArray,target):
        map = {}
        for i in range(len(calcArray)):
            if not map.has_key(calcArray[i]):
                map[target-calcArray[i]] = i
            else:
                return [map[target-calcArray[i]],i]
        return [-1,-1]
