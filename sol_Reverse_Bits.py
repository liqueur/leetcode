

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        queue = list()

        while n:
            queue.append(n % 2)
            n //= 2

        for i in range(32 - len(queue)):
            queue.append(0)

        ret = 0
        for x in queue:
            ret *= 2
            ret += x

        return ret


if __name__ == '__main__':
    sol = Solution()
    ret = sol.reverseBits(43261596)
    print(ret)
