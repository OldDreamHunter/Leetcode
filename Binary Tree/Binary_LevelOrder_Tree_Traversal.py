"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

from collections import deque

class solution(object):
    def __init__(self):
        self.result = list()

    def levelOrderTraversal(self,root):
    # 用deque的popleft来实现queue
        queue = deque([root])
        res = list()
        if root == None:
            return res

        while len(queue) > 0:
            valueQ = len(queue)
            # 每一层运行完curlevel重置
            curLevel = list()
            for eachQ in range(valueQ):
                tempNode = queue.popleft()
                curLevel.append(tempNode.val)
                if tempNode.left != None:
                    queue.append(tempNode.left)
                if tempNode.right != None:
                    queue.append(tempNode.right)
            res.append(curLevel)
        return res

    def levelOrderTraversal(self,root):
        queue = deque([root])
        res = list()
        if root == None:
            return res
        while queue:
            valueQ = len(queue)
            curLevel = list()
            for eachQ in range(valueQ):
                tempNode = queue.popleft()
                curLevel.append(tempNode.val)
                if tempNode.left != None:
                    queue.append(tempNode.left)
                if tempNode.right != None:
                    queue.append(tempNode.right)
                res.append(curLevel)
            res.append(curLevel)
        return res

    def zigzagLevelOrderTraversal(self, root):
        queue = deque([root])
        result = list()
        if not root: return result
        reverse = 0
        while queue:
            curLevel = list()
            valueQ = len(queue)
            for i in range(valueQ):
                tempNode = queue.popleft()
                curLevel.append(tempNode.val)
                if tempNode.left: queue.append(tempNode.left)
                if tempNode.right: queue.append(tempNode.right)
            if reverse:
                curLevel = curLevel[::-1]
                reverse = 0
            else:
                reverse = 1
            result.append(curLevel)
        return result



