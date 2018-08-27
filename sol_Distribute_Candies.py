# coding:utf-8


class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        cand_set = set(candies)
        half = len(candies) // 2

        if len(cand_set) <= half:
            return len(cand_set)

        if len(cand_set) > half:
            return half

sol = Solution()
input = [1,1,2,2,3,3]
output = sol.distributeCandies(input)
print(output)
