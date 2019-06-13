"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""
from collections import Counter

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class solution(object):

    def mergeTwoLists(self, array1, array2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = curr = ListNode(0)
        while array1 and array2:
            if array1.val < array2.val:
                curr = array1
                array1 = array1.next
                curr = curr.next

            else:
                curr = array2
                array2 = array2.next
                curr = curr.next
            curr = curr.next

        if not array1: curr.next = array1
        if not array2: curr.next = array2

        return head


