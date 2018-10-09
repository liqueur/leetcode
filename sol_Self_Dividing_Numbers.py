class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ret = []
        for val in range(left, right + 1):
            if self.check(val):
                ret.append(val)

        return ret

    def check(self, val):
        _val = val

        while val:
            if (val % 10 == 0) or (_val % (val % 10) != 0):
                return False
            val //= 10

        return True
