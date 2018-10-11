
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        from collections import defaultdict

        licensePlate = licensePlate.lower()
        lp_set = set([c for c in licensePlate if c.isalpha()])
        lp_dict = defaultdict(int)

        ret = ''

        for c in list(licensePlate):
            lp_dict[c] += 1

        for w in words:
            _w = w.lower()
            w_set = set(list(_w))

            _set = lp_set & w_set

            if len(_set) == len(lp_set):
                w_dict = defaultdict(int)
                for c in list(_w):
                    w_dict[c] += 1

                b = True
                for c in _set:
                    if lp_dict[c] > w_dict[c]:
                        b = False
                        break

                if b:
                    if not ret or len(w) < len(ret):
                        ret = w

        return ret


sol = Solution()
licensePlate = "GrC8950"
words = ["measure","other","every","base","according","level","meeting","none","marriage","rest"]
ret = sol.shortestCompletingWord(licensePlate, words)
print(ret)
