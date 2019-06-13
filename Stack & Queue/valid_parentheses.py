"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""

class Solution(object):
    def isValid(self, s):
        """
        :param s:
        :return:
        """
        stack = []
        for eachstr in s:
            if eachstr in ['(', '[', '{']:
                stack.append(eachstr)
            elif len(stack) == 0: return False
            if eachstr == ']' and stack.pop() != '[': return False
            if eachstr == ')' and stack.pop() != '(': return False
            if eachstr == '}' and stack.pop() != '{': return False
        if len(stack) > 0: return False
        return True



if __name__ == '__main__':
    solution = Solution()
    if solution.isValid(''): print 'True'
    else: print 'False'




