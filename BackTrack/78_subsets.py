"""
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

Example:
Input: nums = [1,2,3]
Output:
[
  [3],[1],[2],[1,2,3],
  [1,3],[2,3],[1,2],[]
]
"""
class Solution(object):
    def subset(self, nums):
        res = []
        self.dfs(nums, 0, [], res)
        return sorted(res)

    def dfs(self, nums, index, path, res):
        if path not in res:
            res.append(path)
        for eachindex in range(index, len(nums)):
            if nums[eachindex] not in path:
                self.dfs(nums, eachindex+1, path+[nums[eachindex]], res)


class Solution2(object):
    def subset1(self, nums):
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]], res)

if __name__ == '__main__':
    solution = Solution()
    print(solution.subset([1,2,3]))

