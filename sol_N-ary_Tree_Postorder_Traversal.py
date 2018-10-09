class Solution(object):
    def postorder(self, root):
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