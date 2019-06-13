"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

"""
import string

class solution(object):
    def firstUniq(self, s):
        letters = string.ascii_lowercase
        result = [s.index(l) for l in letters if s.count(l) == 1]
        return min(result) if len(result) > 0 else -1


if __name__ == '__main__':
    problem = solution()
    print problem.firstUniq('aaasiied')
