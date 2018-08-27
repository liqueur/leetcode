#coding:utf-8


class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        map = {n: -1 for n in nums}
        for i, x in enumerate(nums):
            for j, y in enumerate(nums):
                if j > i and y > x:
                    map[x] = y
                    break

        return [map[n] for n in findNums]


sol = Solution()
output = sol.nextGreaterElement([4,1,2], [1,3,4,2])
print(output)
