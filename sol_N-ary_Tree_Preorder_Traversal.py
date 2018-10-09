"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        container = []
        if not root:
            return container

        self.traverse(root, container)
        return container

    def traverse(self, node, container):
        for child in node.children:
            self.traverse(child, container)
        container.append(node.val)
