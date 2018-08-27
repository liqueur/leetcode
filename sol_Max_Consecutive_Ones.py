# coding:utf-8


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 0
        cur_len = 0
        for k, n in enumerate(nums):
            if n == 1:
                cur_len += 1

            if n == 0:
                if cur_len > max_len:
                    max_len = cur_len
                cur_len = 0

        if cur_len > max_len:
            max_len = cur_len

        return max_len


sol = Solution()
output = sol.findMaxConsecutiveOnes([1,1,0,1,1,1])
print(output)
