

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = _sum = 0

        _len = len(digits)
        for j in range(_len):
            _sum += digits[_len - j - 1] * (10 ** i)
            i += 1

        _sum += 1

        if _sum != 10 ** i:
            i -= 1

        ret = []

        if _sum == 0:
            return [0]

        while i >= 0:
            v = _sum // (10 ** i)
            _sum -= v * (10 ** i)
            ret.append(v)
            i -= 1

        return ret


sol = Solution()
ret = sol.plusOne([3])
print(ret)
