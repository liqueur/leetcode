# coding:utf-8

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        cnt = 0

        for row in nums:
            cnt += len(row)

        if cnt != (r * c):
            return nums

        queue = []

        for row in nums:
            for elem in row:
                queue.append(elem)

        matrix = []

        for i in range(r):
            n = 0
            row = []
            while n < c:
                row.append(queue.pop(0))
                n += 1

            matrix.append(row)

        return matrix


sol = Solution()
input = ([[1,2], [3,4]], 1, 4)
output = sol.matrixReshape(*input)
print(output)
