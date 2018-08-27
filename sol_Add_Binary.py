

class Solution:
    def bin2int(self, val):
        _sum = i = 0
        _val = list(val)
        _len = len(_val)

        for j in range(_len):
            v = 0 if _val[_len - j - 1] == '0' else 1
            _sum += v * 2 ** i
            i += 1

        return _sum

    def int2bin(self, val):
        _bin = ''
        if val == 0:
            return '0'

        while val:
            _bin = ('0' if val % 2 == 0 else '1') + _bin
            val //= 2

        return _bin

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return self.int2bin(self.bin2int(a) + self.bin2int(b))
