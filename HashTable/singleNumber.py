"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""
class solution(object):
    def singleNum(self,numList):
        """
        :process: check the table for eachnum, if in, pop, else, append
        :param numList:
        :return:
        """
        hashtable = {}
        for eachnum in numList:
            try:
                hashtable.pop(eachnum)
            except:
                hashtable[eachnum] = 1
        return hashtable.popitem()[0]

    def singleNum(self,numlist):
        a = 0
        for eachnum in numlist:
            a ^= eachnum
        return a