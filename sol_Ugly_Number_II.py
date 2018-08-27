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
        nums = [0 for i in range(1691)]
        nums[1] = 1
        i = 0
        cnt = 0
        while cnt < n:
            i += 1
            if nums[i] == 1:
                if i * 2 < 1691:
                    nums[i * 2] = 1

                if i * 3 < 1691:
                    nums[i * 3] = 1

                if i * 5 < 1691:
                    nums[i * 5] = 1

                cnt += 1
                print(cnt, i)

        return i

sol = Solution()
ret = sol.nthUglyNumber(103)
print(ret)
