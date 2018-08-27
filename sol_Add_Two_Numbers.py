
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        _sum = 0
        l1stk = []
        l2stk = []

        while l1 or l2:
            if l1:
                l1stk.append(l1.val)
                l1 = l1.next

            if l2:
                l2stk.append(l2.val)
                l2 = l2.next

        i = 0
        while l1stk or l2stk:
            l1v = l1stk.pop(0) if l1stk else 0
            l2v = l2stk.pop(0) if l2stk else 0

            _sum += (l1v + l2v) * (10 ** i)

            i += 1

        root = pre = None
        while _sum or (root is None):
            v = _sum % 10
            _sum //= 10
            if pre is None:
                root = pre = ListNode(v)
            else:
                cur = ListNode(v)
                pre.next = cur
                pre = cur

        return root
