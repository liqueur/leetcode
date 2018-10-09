import math

"""
Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0

        p = [1 for i in range(n)]
        p[0] = p[1] = 0
        i = 2
        cnt = 0

        while i * i <= n:
            for j in range(i + i, n, i):
                p[j] = 0
            i += 1

        for k in range(len(p)):
            if p[k] == 1:
                cnt += 1

        return cnt


sol = Solution()
ret = sol.countPrimes(1500000)
print(ret)
