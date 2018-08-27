# coding:utf-8


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        queue = []
        queue.append((0, root))
        ret = {}

        while queue:
            level, node = queue.pop(0)
            ret.setdefault(level, [])
            ret[level] = node.val

            level += 1

            if node.left:
                queue.append((level, node.left))

            if node.right:
                queue.append((level, node.right))

        return [sum(ret[k]) / len(ret[k]) for k in sorted(ret.keys())]