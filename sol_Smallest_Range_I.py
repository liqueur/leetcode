class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A = sorted(A)
        _min = A[0]
        _max = A[-1]

        return 0 if _max - _min <= 2 * K else _max - _min - 2 * K
