# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        container1 = []
        container2 = []
        self.traverse(root1, container1)
        self.traverse(root2, container2)

        if len(container1) != len(container2):
            return False
        else:
            for i, _ in enumerate(container1):
                if container1[i] != container2[i]:
                    return False

        return True

    def traverse(self, node, container):
        if not node:
            return

        self.traverse(node.left, container)
        self.traverse(node.right, container)
        if not node.left and not node.right:
            container.append(node.val)
