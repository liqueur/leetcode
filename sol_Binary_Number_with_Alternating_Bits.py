
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """

        bits = []

        while n:
            bits.insert(0, n % 2)
            n //= 2

        x = bits[0]
        for i in range(1, len(bits)):
            if bits[i] + x != 1:
                return False
            else:
                x = bits[i]

        return True


args = (11, )
sol = Solution()
ret = sol.hasAlternatingBits(*args)
print(ret)

