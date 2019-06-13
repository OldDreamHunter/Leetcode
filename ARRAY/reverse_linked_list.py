"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        while curr != None:
            tempNode = curr.next
            curr.next = prev
            prev = curr
            curr = tempNode
        return prev

    def insertList(self, inputList=[1, 2, 3, 4, 5]):
        head = ListNode(1)
        curr = head
        for eachitem in inputList[1:]:
            curr.next = ListNode(eachitem)
            curr = curr.next
        return head

    def printList(self, head):
        curr = head
        while curr.next:
            print curr.val


solution = Solution()
calcList = solution.insertList()
resultList = solution.reverseList(calcList)
solution.printList(resultList)


class solution(self):
    def reverseLinkedList(self,head):
        if not head:
            return None
        else:
            prev = None
            while head:
                curr = head
                head = head.next
                curr.next = prev
                prev = curr
        return curr
