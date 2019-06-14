"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

import numpy.array as array


class binaryTree(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class solution(object):
    def recursivePreOrderTraversal(self, root):
        """
        :param root:
        :return:
        """
        # 如果该节点为None则返回
        # 否则就打印根结点，然后再依次访问左子树和右子树
        if root == None:
            return
        print root.val
        preOrderTraversal(root.left)
        preOrderTraversal(root.right)

        # 栈是先入后出，队列是先进先出

    def preOrderTravel(self, root):
        stack = list()
        if root == None:
            return
        stack.append(root)
        while stack:
            valNode = stack.pop()
            print valNode.val
            if valNode.right != None:
                stack.append(valNode.right)
            elif valNode.left != None:
                stack.append(valNode.left)

    def preorderTraversal(self, root):
        stack = list()
        result = list()
        stack.append(root)
        if not root: return result
        while stack:
            curr = stack.pop()
            result.append(curr.val)
            if curr.right: stack.append(curr.right)
            if curr.left: stack.append(curr.left)
        return result
