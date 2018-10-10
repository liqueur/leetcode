class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        letters = 'abcdefghijklmnopqrstuvwxyz'
        _width = {}

        for i, c in enumerate(letters):
            _width[c] = widths[i]

        row = 1
        col = 0
        for c in S:
            if col + _width[c] > 100:
                row += 1
                col = _width[c]
            else:
                col += _width[c]

        return [row, col]


sol = Solution()
ret = sol.numberOfLines([5,7,4,7,6,7,9,5,8,8,5,10,9,10,2,5,7,9,3,8,8,8,10,2,2,9], "lgrnv")
print(ret)