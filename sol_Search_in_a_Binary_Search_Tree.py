# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return

        return self.search(root, val)

    def search(self, node, val):
        if node.val == val:
            return node

        if node.val > val and node.left:
            return self.search(node.left, val)

        if node.val < val and node.right:
            return self.search(node.right, val)
