# coding=utf-8
"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

"""
class solution(object):
    def majorityElementHash(self,nums):
        hashtable = {}
        maximum = 0
        maxkey = 0
        for i in nums:
            if not hashtable.has_key(i):
                hashtable[i] = 0
            hashtable[i] += 1
            if hashtable[i] > maximum:
                maximum,maxkey = hashtable[i],i
        return maxkey

    def majorityElementVote(self,nums):
        countMaj = 0
        for i in range(len(nums)):
            if countMaj == 0:
                majority = nums[i]
                countMaj += 1
            else:
                countMaj += (1 if nums[i] == majority else -1)
        return majority

if __name__ == '__main__':
    solve = solution()
    print solve.majorityElementHash([3,3,4])
    print solve.majorityElementVote([3,3,4])