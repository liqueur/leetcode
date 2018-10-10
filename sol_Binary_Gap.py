
class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        bits = self.to_bits(N)

        _list = []
        dist = [0, ]

        for i, b in enumerate(bits):
            if b == 1:
                _list.append(i)

        for i in range(len(bits)):
            if bits[i] == 1:
                for j in range(i, len(bits)):
                    if i != j and bits[j] == 1:
                        dist.append(j - i)
                        break

        return max(dist)

    def to_bits(self, val):
        bits = []

        while val:
            bits.insert(0, val % 2)
            val //= 2

        return bits
