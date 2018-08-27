# coding:utf-8

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 0
        m = 0
        while num:
            if num & 1 > 0:
                pass
            else:
                m += 2 ** i
            num >>= 1
            i += 1

        return m


sol = Solution()
ret = sol.findComplement(5)

print(ret)
