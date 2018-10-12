
class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)

        max1 = max2 = max3 = -2000
        min1 = min2 = 2000

        for n in nums:
            if n > max1:
                max1, max2, max3 = n, max1, max2
            elif n > max2:
                max2, max3 = n, max2
            elif n > max3:
                max3 = n

            if n < min1:
                min1, min2 = n, min1
            elif n < min2:
                min2 = n

        return max(max1 * min1 * min2, max1 * max2 * max3)
