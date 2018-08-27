"""
Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:

1 is typically treated as an ugly number.
n does not exceed 1690.
"""

class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        n2 = n3 = n5 = 0
        i = 1
        last = 1
        ugly = [1]

        while i < n:
            new = min(ugly[n2] * 2, ugly[n3] * 3, ugly[n5] * 5)
            if new == ugly[n2] * 2:
                n2 += 1
            if new == ugly[n3] * 3:
                n3 += 1
            if new == ugly[n5] * 5:
                n5 += 1
            if new > last:
                i += 1
                last = new
                ugly.append(last)

        return last


sol = Solution()
ret = sol.nthUglyNumber(1691234)
print(ret)
