# coding=utf-8

"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

"""

class solution(object):
    def anagram(self,s1,s2):
        hashtable = {}
        for i in s1:
            if i in hashtable: hashtable[i] += 1
            else: hashtable[i] = 1

        for i in s2:
            if i in hashtable: hashtable[i] -= 1
            else: return False

        for eachvalue in hashtable.values():
            if eachvalue != 0 : return False

        return True