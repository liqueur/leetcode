class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        if not num:
            return num

        n = 0
        while num:
            n += num % 10
            num //= 10
            if num == 0:
                if n >= 10:
                    num = n
                    n = 0
                else:
                    break

        return n



sol = Solution()
ret = sol.addDigits(1111)
print(ret)