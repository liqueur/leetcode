

class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        L, R = 0, len(S) - 1
        ss = list(S)
        while L < R:
            if ss[L].isalpha() and ss[R].isalpha():
                ss[L], ss[R] = ss[R], ss[L]
                L += 1
                R -= 1

            if not ss[L].isalpha():
                L += 1

            if not ss[R].isalpha():
                R -= 1

        return ''.join(ss)


sol = Solution()
ret = sol.reverseOnlyLetters("Test1ng-Leet=code-Q!")
print(ret)
