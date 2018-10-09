"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        ret = []
        queue = []

        if not root:
            return ret

        queue.append((root, 0))

        while queue:
            node, level = queue.pop(0)
            if level >= len(ret):
                ret.append([])
            ret[level].append(node.val)
            for child in node.children:
                queue.append((child, level + 1))

        return ret
