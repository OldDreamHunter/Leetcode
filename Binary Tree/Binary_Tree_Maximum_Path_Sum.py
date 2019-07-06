"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to
any node in the tree along the parent-child connections. The path must contain at least
one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""

# recursive solution of the problems
class solution(object):

    # recursive method
    def maxend(self,root):
        if not root: return 0
        if not (root.left or root.right): return root.val
        else:
            if root.val >= 0:
                result = root.val + max(self.maxend(root.right), 0) + max(self.maxend(root.left), 0)
            else:
                result = root.val
            return max(self.maxend(root.left), self.maxend(root.right), result)

    # iterative method(DFS)
    def maximumPathSum(self,root):
        stack = list()
        result = list()
        if not root: return None
        else:
            stack.append(root)
            tempNode = root
        while len(stack) > 0 and tempNode:
            while tempNode:
                tempNode = tempNode.left
                if tempNode: stack.append(tempNode)
            tempNode = stack.pop()
            result.append(tempNode.val)
            tempNode = tempNode.right





