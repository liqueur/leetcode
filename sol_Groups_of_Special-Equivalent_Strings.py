

class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        _dict = {}

        for a in A:
            k = ''.join(sorted(a))
            _dict.setdefault(k, [])
            _dict[k] = a

        print(_dict)


sol = Solution()
sol.numSpecialEquivGroups(["abc","acb","bac","bca","cab","cba"])
