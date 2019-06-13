"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""
from collections import deque

class solution(object):

    def __init__(self):
        self.depth = 0

    def recurseMaximumDepth(self,root):
        if not root:
            return 0
        else:
            MRDepth = self.recurseMaximumDepth(root.right) + 1
            MLDepth = self.recurseMaximumDepth(root.left) + 1
        return max(MRDepth,MLDepth)

    def maxiMumDepth(self,root):
        if not root:
            return 0
        else:
            tempQ = deque([(root,1)])
            while tempQ:
                tempNode,val = tempQ.popleft()
                if tempNode.left: tempQ.append([tempNode.left,val+1])
                if tempNode.right: tempQ.append([tempNode.right,val+1])
            return val




