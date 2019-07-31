# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prenode = None
        currnode = head
        if currnode == None: return None
        while currnode:
            tempnode = currnode.next
            currnode.next = prenode
            prenode = currnode
            currnode = tempnode
        return prenode
