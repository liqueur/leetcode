
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        from collections import defaultdict

        a_words = defaultdict(int)
        b_words = defaultdict(int)

        for w in A.split(' '):
            a_words[w] += 1

        for w in B.split(' '):
            b_words[w] += 1

        ret = []

        for k in a_words:
            if a_words[k] == 1 and k not in b_words:
                ret.append(k)

        for k in b_words:
            if b_words[k] == 1 and k not in a_words:
                ret.append(k)

        return ret



sol = Solution()
A = "apple apple"
B = "banana"
ret = sol.uncommonFromSentences(A, B)
print(ret)

