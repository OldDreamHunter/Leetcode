"""
是否回文数
"""
class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        i,j = 0,len(x)
        while i<j:
            if x[i] != x[j]: return False
        return True
