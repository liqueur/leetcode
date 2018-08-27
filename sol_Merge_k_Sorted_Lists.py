"""
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def traverse(self, tree, rs):
        if not tree:
            return

        if tree.left:
            self.traverse(tree.left, rs)

        rs.append(tree.val)

        if tree.right:
            self.traverse(tree.right, rs)

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        root = None
        for i in range(len(lists)):
            while lists[i]:
                node = TreeNode(lists[i].val)
                if root is None:
                    root = node
                else:
                    pre = cur = root
                    while cur:
                        pre = cur
                        if node.val <= cur.val:
                            cur = cur.left
                        else:
                            cur = cur.right

                    if node.val <= pre.val:
                        pre.left = node
                    else:
                        pre.right = node

                lists[i] = lists[i].next

        rs = []
        self.traverse(root, rs)
        pre = root = None

        for i in range(len(rs)):
            cur = ListNode(rs[i])
            if root is None:
                root = pre = cur
            else:
                pre.next = cur
                pre = cur

        return root
