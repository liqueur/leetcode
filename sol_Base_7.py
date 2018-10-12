
class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'

        n = abs(num)
        ret = list()

        while n:
            ret.insert(0, str(n % 7))
            n //= 7

        if num < 0:
            ret.insert(0, '-')

        return ''.join(ret)

