"""
find the median of two sorted lists
"""
from numpy import median


class solution(object):
    def medianoflists(self,s1,s2):
        if len(s1) == 0: return median(s2)
        if len(s2) == 0: return median(s1)
        m = len(s1)
        n = len(s2)
        i = 1
        j = int((m+n)/2) - i
        while i >= 0 and i < n and j >= 0 and j < m:
            if s1[i-1] <= s2[j] and s2[j-1] <= s1[i]:
                if (m+n)%2:
                    return max(s1[i-1],s2[j-1])
                else:
                    return (max(s1[i-1], s2[j-1])+min(s1[i], s2[j]))/2
            if s1[i-1] > s2[j]:
                i = i - 1
            if s1[i] < s2[j-1]:
                i = i + 1
            j = int((m+n)/2) - i
        if i < 0 or i > m: return s2[j]
        else: return s1[i]

if __name__ == '__main__':
    s1 = [1,2,5]
    s2 = [2,4,7,8]
    problem = solution()
    print(problem.medianoflists(s1, s2))

