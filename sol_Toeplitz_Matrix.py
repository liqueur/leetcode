

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        nr = len(matrix)
        nc = len(matrix[0])

        from collections import defaultdict

        matrix_dict = defaultdict(list)

        for r in range(nr):
            for c in range(nc):
                r0 = r - min(r, c)
                c0 = c - min(r, c)
                matrix_dict[(r0, c0)].append(matrix[r][c])

        for k in matrix_dict:
            t = matrix_dict[k][0]
            for x in matrix_dict[k]:
                if t != x:
                    return False

        return True


matrix = [
    [1, 2, 3, 4],
    [5, 1, 2, 3],
    [9, 5, 1, 2]
]
matrix = [
  [1,2],
  [2,2]
]
sol = Solution()
ret = sol.isToeplitzMatrix(matrix)
print(ret)