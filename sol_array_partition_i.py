# coding:utf-8


'''
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
'''
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return sum([n for i, n in enumerate(nums) if i % 2 == 0])



sol = Solution()
ret = sol.arrayPairSum([1, 4, 3, 2])
print(ret)
