"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

"""

class solution(object):
    def maximumSubarray(self,nums):
        currSum = maxSum = 0
        for i in range(len(nums)):
            currSum = max(nums[i], currSum+nums[i])
            maxSum = max(maxSum, currSum)
        return maxSum

if __name__ == '__main__':
    problem = solution()
    print problem.maximumSubarray([1,2,3,-1,-2,9,10])