# coding:utf-8

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b:
            carry = a & b
            a ^= b
            b = carry << 1

        return a



sol = Solution()
ret = sol.getSum(100, 200)
print(ret)
