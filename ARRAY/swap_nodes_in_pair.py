"""

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.

"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swap_nodes(self, head):
        curr = head
        nextNode = curr.next
        while curr and nextNode:
            tempVal = curr.val
            curr.val = nextNode.val
            nextNode.val = tempVal
            curr = nextNode.next
            if curr is None: break
            nextNode = curr.next
        return head

    def insertList(self, inputList=[1, 2, 3, 4, 5]):
        head = ListNode(1)
        curr = head
        for eachitem in inputList[1:]:
            curr.next = ListNode(eachitem)
            curr = curr.next
        return head

solution = Solution()
calclist = solution.insertList([1,2,3,4,5])
resultlist = solution.swap_nodes(calclist)
print 'end'
