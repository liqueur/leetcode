"""
Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = pre = None

        while l1 and l2:
            if l1.val < l2.val:
                next = l1
                l1 = l1.next
            else:
                next = l2
                l2 = l2.next

            if root is None:
                root = pre = next
            else:
                pre.next = next
                pre = next

        while l1:
            if root is None:
                root = pre = l1
            else:
                pre.next = l1
                pre = l1

            l1 = l1.next

        while l2:
            if root is None:
                root = pre = l2
            else:
                pre.next = l2
                pre = l2

            l2 = l2.next

        return root
