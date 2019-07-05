"""
given binary tree
find its maximum depth
"""

class treeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class solution(object):
    def max_recursive(self, root):
        if root == None:
            return 0
        depth = max(self.max_recursive(root.left), self.max_recursive(root.right)) + 1
        return depth

    def max_iterative(self, root):
        stack = []
        maxdepth = 0
        if root != None:
            stack.append([root,1])
        while stack:
            node, curdepth = stack.pop()
            maxdepth = max(maxdepth,curdepth)
            if node.left: stack.append([node.left, curdepth+1])
            if node.right: stack.append([node.right, curdepth+1])
        return maxdepth
