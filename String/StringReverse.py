"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""


class solution(object):

    def recurseReverse(self, s):
        if len(s) <= 1:
            return s
        l = len(s)
        return self.recurseReverse(s[l/2:]) + self.recurseReverse(s[:l/2])

    def Reverse(self,s):
        l = len(s)
        i,j = 0,l-1
        while i<j:
            s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1
        return s

if __name__ == '__main__':
    reverse = solution()
    print reverse.Reverse(['1','2','3','4','5','6','7','8'])