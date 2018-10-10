# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root

        new = {'root': None, 'node': None}
        self.traverse(root, new)
        return new['root']

    def traverse(self, node, new):
        if not node:
            return

        self.traverse(node.left, new)

        if new['root'] is None:
            new['root'] = new['node'] = TreeNode(node.val)
        else:
            new['node'].right = TreeNode(node.val)
            new['node'] = new['node'].right

        self.traverse(node.right, new)
