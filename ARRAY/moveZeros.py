"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""

class solution(object):
    def moveZeros(self,numList):
        zeros = 0
        for eachnum in range(len(numList)):
            if numList[eachnum] != 0:
                numList[zeros],numList[eachnum]=numList[eachnum],numList[zeros]
                zeros += 1
        return numList

