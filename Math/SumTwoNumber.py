"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1

Bit Manipulation
"""

class solution(object):
    def sumOperator(self,a,b):
        return (a^b) ^ ((a&b)<<1)

if __name__ == '__main__':
    problem = solution()
    print(problem.sumOperator(20,30))
