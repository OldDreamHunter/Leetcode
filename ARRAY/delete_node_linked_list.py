# -*- coding=utf-8 -*-
"""
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:

Example 1:

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
Example 2:

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.


deletNode 其实就是把当前节点替换为下一个节点
如果下一个节点是空，当前节点直接替换为空；
如果下一个节点不为空，就是当前节点的值替换为下一个节点的值，并且当前节点的下一个链接替换为下一个节点
"""

class solution(object):
    def stupidDeleteNode(self,head,node):
        """
        :param node:
        :return:
        """
        cur = head
        prev = None
        while cur:
            if cur.val == node and (not prev):
                temp = cur.next
                cur.next = None
                cur = temp
            elif cur.val == node and prev:
                prev.next = cur.next
                cur.next = None
            prev = cur
            cur = cur.next

    def deleteNode(self,node):
        """
        :return:
        """
        node.val, node.next = node.next.val, node.next.next

