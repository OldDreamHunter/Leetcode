"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed)
in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


"""
hashmap for the node tracking with O(n) memory
"""


class Solution1(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodeDict = set()
        curr = head
        nodeDict.append(curr)
        while curr:
            temp = curr.next
            if temp == None: return False
            if curr in nodeDict:
                return True
            else:
                nodeDict[temp] = 0
            curr = temp
        return False


"""
double node, one fast and one slow
"""


class Solution2(object):
    def hasCycle(self, head):
        fastNode = head
        slowNode = None
        while fastNode:
            if slowNode == fastNode:
                return True
            if slowNode is None:
                slowNode = head
            if fastNode.next is None:
                return False
            else:
                fastNode = fastNode.next.next
                slowNode = slowNode.next
        return False
