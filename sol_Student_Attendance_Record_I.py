

class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """

        ac = lc = 0
        s += ' '

        for ss in s:
            if ss == 'A':
                ac += 1
                if ac > 1:
                    return False
                lc = 0
            if ss == 'L':
                lc += 1
                if lc > 2:
                    return False
            if ss == 'P':
                lc = 0

        return True
