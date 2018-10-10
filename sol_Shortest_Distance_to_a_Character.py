

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        T = []
        for i, s in enumerate(S):
            if s == C:
                T.append(i)

        ret = []
        for i, s in enumerate(S):
            ret.append(min([abs(i - t) for t in T]))

        return ret
