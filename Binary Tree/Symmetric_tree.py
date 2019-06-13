"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
"""

class solution(object):
    def symmeticTreeRecurs(self, tree1, tree2):
        if tree1 == None and tree2 == None: return True
        if tree1 == None and tree2 != None: return False
        if tree1 != None and tree2 == None: return False
