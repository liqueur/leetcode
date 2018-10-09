class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        mi = 0

        for i, x in enumerate(A):
            if x > A[mi]:
                mi = i

        return mi

