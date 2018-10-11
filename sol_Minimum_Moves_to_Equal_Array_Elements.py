
class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minval = nums[0]
        res = 0

        for n in nums:
            minval = min(n, minval)

        for n in nums:
            res += n - minval

        return res
