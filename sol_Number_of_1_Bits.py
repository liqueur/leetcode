

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0

        while n:
            ret += n % 2
            n //= 2

        return ret
