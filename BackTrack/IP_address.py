"""
Given a string containing only digits, restore it by returning all
possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""

class solution(object):
    def restoreIpAddresses(self, s):
        output = []
        self.backtrack(s, 0, '', output)
        return output

    def backtrack(self, combinationstr, index, appendstr, output):
        if index == 4:
            if not combinationstr: output.append(appendstr[:-1])
        else:
            for i in range(1, 4):
                if i <= len(combinationstr):
                    if i == 1:
                        self.backtrack(combinationstr[i:], index+1, appendstr+combinationstr[:i]+'.', output)
                    elif i == 2 and combinationstr[0] != '0':
                        self.backtrack(combinationstr[i:], index+1, appendstr+combinationstr[:i]+'.', output)
                    elif i == 3 and combinationstr[0] != '0' and int(combinationstr[:3]) <= 255:
                        self.backtrack(combinationstr[i:], index+1, appendstr+combinationstr[:i]+'.', output)


