# coding:utf-8

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map = {}
        for n in nums:
            map.setdefault(n, 0)
            map[n] += 1

        for k in map:
            if map[k] == 1:
                return k
