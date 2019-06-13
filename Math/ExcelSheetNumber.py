"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
"""

class solution(object):
    def titleNumber(self,s):
        if s == '': return 0
        tn = 0
        for i in range(len(s)):
            tn += pow(26,len(s)-i-1) * (ord(s[i])-ord('A')+1)
        return tn

    def titleToNumber(self,s):
        return sum([pow(26, len(s) - i - 1) * (ord(s[i]) - ord('A') + 1) for i in range(len(s))])

if __name__ == '__main__':
    problem1 = solution()
    print(problem1.titleNumber('AB'))

