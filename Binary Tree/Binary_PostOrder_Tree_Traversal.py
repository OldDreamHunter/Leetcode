"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
class nodeTree(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.list = list()

    def recursPostOrderTree(self,root):
        if root == None:
            return
        self.recursPostOrderTree(root.left)
        self.recursPostOrderTree(root.right)
        self.list.append(root.val)
        return self.list
