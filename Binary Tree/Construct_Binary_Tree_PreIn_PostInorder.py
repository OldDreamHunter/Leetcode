"""
Given inorder and postorder traversal of a tree, construct the binary tree.
Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class solution(object):
    def buildTreeInPost(self, inorder, postorder):
        if len(inorder) == 0 or len(postorder) == 0:
            return None
        val = postorder.pop()
        mid = inorder.index(val)
        root = TreeNode(val)
        root.left = self.buildTreeInPost(inorder[:mid], postorder)
        root.right = self.buildTreeInPost(inorder[mid+1:], postorder)
        return root

    def buildTreePreIn(self, preorder, inorder):
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        val = preorder.pop(0)
        mid = inorder.index(val)
        root = TreeNode(val)
        root.left = self.buildTreePreIn(preorder, inorder[:mid])
        root.right = self.buildTreePreIn(preorder, inorder[mid+1:])
        return root


if __name__ == '__main__':
    problem = solution()
    root = problem.buildTreeInPost([9,3,15,20,7],[9,15,7,20,3])
    root = problem.buildTreePreIn()