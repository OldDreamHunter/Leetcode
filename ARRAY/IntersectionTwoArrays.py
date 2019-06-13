# coding=utf-8
"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
"""

class solution(object):

    def intersectionTwoArrays(self, array1, array2):
        hashtable = {}
        for i in array1:
            if i in hashtable: hashtable[i] += 1
            else: hashtable[i] = 1

        result = []
        for i in array2:
            if i in hashtable and hashtable[i]>0:
                result.append(i)
                hashtable[i] -= 1

        return result


if __name__ == '__main__':
    problem = solution()
    print problem.intersectionTwoArrays([1,2,3,3,4,5],[3,3,2,9])



