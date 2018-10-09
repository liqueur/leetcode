

class Solution:
    def count_bit(self, x):
        ret = 0
        while x:
            ret += x % 2
            x //= 2
        return ret

    def check_prime(self, x, prime_dict):
        if x in prime_dict:
            return prime_dict[x]

        for n in range(2, x):
            if x % n == 0:
                prime_dict[x] = 0
                return prime_dict[x]
        else:
            prime_dict[x] = 1
            return prime_dict[x]

    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        prime_dict = {1: 0}
        prime_list = list()
        for x in range(L, R + 1):
            prime_list.append(self.check_prime(self.count_bit(x), prime_dict))

        return sum(prime_list)
