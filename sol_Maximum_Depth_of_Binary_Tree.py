# coding:utf-8


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        queue = []
        queue.append((1, root))
        depth = 0

        while queue:
            level, node = queue.pop(0)
            if level > depth:
                depth = level

            if node.left:
                queue.append((level + 1, node.left))

            if node.right:
                queue.append((level + 1, node.right))

        return depth
