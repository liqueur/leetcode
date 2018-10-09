"""
Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""


class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(2, n + 1):
            if n - i * i > 0:
                ret = self.numSquares(n - i * i)
                print(i, ret)
            else:
                return n - i * i


sol = Solution()
sol.numSquares(12)
