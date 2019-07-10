"""
find the kthSmallest node from the tree
"""
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        result = []
        if not root: return None
        stack.append(root)
        curr = root
        while stack:
            while curr:
                curr = curr.left
                if curr: stack.append(curr)
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
            if curr: stack.append(curr)
            if len(result) == k: break
        return result[-1]




