
class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict

        degree = defaultdict(int)
        scope = dict()

        for i, n in enumerate(nums):
            degree[n] += 1
            if n not in scope:
                scope[n] = [i, i]
            else:
                scope[n][1] = i

        mn = max(degree.values())
        minnums = list()

        for k in degree:
            if degree[k] == mn:
                minnums.append(k)

        return min([scope[n][1] - scope[n][0] + 1 for n in minnums])
