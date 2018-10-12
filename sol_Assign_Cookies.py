class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """

        g = sorted(g)
        s = sorted(s)
        i = 0
        res = 0

        for ss in s:
            if i < len(g) and ss >= g[i]:
                res += 1
                i += 1

        return res
