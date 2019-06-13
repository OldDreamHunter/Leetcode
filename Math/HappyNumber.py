"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

class solution(object):
    def happyNumber(self,inputNum):
        mem = inputNum
        tempResult = set()
        while mem!=1:
            tempResult.add(mem)
            mem = sum([int(eachnum) ** 2 for eachnum in str(mem)])
            if mem in tempResult: return False
        return True


if __name__ == '__main__':
    problem = solution()
    print problem.happyNumber(29)