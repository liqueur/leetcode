

class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        """
        2 -> 5 
        5 -> 2
        6 -> 9
        9 -> 6
        """

        digits = list()

        for x in range(1, N + 1):
            xx = str(x)
            if ('2' in xx) or ('5' in xx) or ('6' in xx) or ('9' in xx):
                if ('3' not in xx) and ('4' not in xx) and ('7' not in xx):
                    digits.append(x)

        return len(digits)
