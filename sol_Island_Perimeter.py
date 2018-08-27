# coding:utf-8


'''
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
'''

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_len = len(grid)
        col_len = len(grid[0])

        perimeter = 0
        for i, row in enumerate(grid):
            for j, elem in enumerate(row):
                if elem == 0:
                    if i - 1 >= 0 and grid[i - 1][j] == 1:
                        perimeter += 1
                    if i + 1 < row_len and grid[i + 1][j] == 1:
                        perimeter += 1
                    if j - 1 >= 0 and grid[i][j - 1] == 1:
                        perimeter += 1
                    if j + 1 < col_len and grid[i][j + 1] == 1:
                        perimeter += 1

                if elem == 1:
                    if i == 0:
                        perimeter += 1
                    if i == row_len - 1:
                        perimeter += 1
                    if j == 0:
                        perimeter += 1
                    if j == col_len - 1:
                        perimeter += 1


        return perimeter


sol = Solution()
input = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

output = sol.islandPerimeter(input)
print(output)
