# coding:utf-8


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        r1 = set(list('qwertyuiop'))
        r2 = set(list('asdfghjkl'))
        r3 = set(list('zxcvbnm'))

        res = []

        for w in words:
            sw = set(list(w.lower()))
            if not (sw - r1):
                res.append(w)
            elif not (sw - r2):
                res.append(w)
            elif not (sw - r3):
                res.append(w)

        return res

sol = Solution()
ret = sol.findWords(["Hello", "Alaska", "Dad", "Peace"])
print(ret)

