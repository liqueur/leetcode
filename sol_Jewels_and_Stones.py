
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        _set = set()
        ret = 0

        for c in J:
            _set.add(c)

        for c in S:
            if c in _set:
                ret += 1

        return ret
