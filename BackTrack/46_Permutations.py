"""
[1,2,3]的全排列
"""
class solution(object):
    def permutation(self,nums):
        res = []
        self.backtrack(nums, [], res)
        return res

    def backtrack(self, nums, path, res):
        if len(path) == len(nums):
            res.append(path)
        else:
            for eachnum in list(set(nums)-set(path)):
                self.backtrack(nums, path+[eachnum], res)

if __name__ == '__main__':
    problem = solution()
    print(problem.permutation([1,2,3,4]))

