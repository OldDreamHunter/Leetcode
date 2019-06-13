"""
Pascal Triangle

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class solution(object):
    def pascalTriangle(self, num):
        triangle = []
        for i in range(num):
            row = [None for _ in range(i + 1)]
            row[0], row[-1] = 1, 1
            if i <= 1:
                triangle.append(row)
                continue
            for tempNum in range(1, i):
                row[tempNum] = triangle[i - 1][tempNum - 1] + triangle[i - 1][tempNum]
            triangle.append(row)
        return triangle

if __name__ == '__main__':
    problem = solution()
    print problem.pascalTriangle(5)
