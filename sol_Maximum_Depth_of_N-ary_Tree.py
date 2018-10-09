"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0

        return self.__max_depth(root, 1)

    def __max_depth(self, node, level):
        if not node:
            return level

        depths = []
        for child in node.children:
            depths.append(self.__max_depth(child, level + 1))

        depths.append(level)

        return max(depths)
