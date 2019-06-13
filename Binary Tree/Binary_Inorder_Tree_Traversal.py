class Node(object):
    def __init__(self,x):
        self.val = x
        self.right = None
        self.left = None
        self.result = list()


class Solution(object):
    def __init__(self):
        self.result = list()
        self.stack = list()

    def recursinorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return
        self.inorderTraversal(root.left)
        self.result.append(root.val)
        self.inorderTraversal(root.right)
        return self.result

    def inorderTraversal(self, root):
        temp = root
        while (temp != None or len(self.stack) > 0):
            while (temp != None):
                self.stack.append(temp)
                temp = temp.left
            temp = self.stack.pop()
            self.result.append(temp.val)
            temp = temp.right
        return self.result






