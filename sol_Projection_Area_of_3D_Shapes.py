
class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # x面，取矩阵非零数量
        # y面，取每列最大数，求和
        # z面，取每行最大数，求和
        nr = len(grid)
        nc = len(grid[0])

        cnt_x = 0
        cnt_y = 0
        cnt_z = 0

        cols = list()

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] > 0:
                    cnt_x += 1

                if c >= len(cols):
                    cols.append([])

                cols[c].append(grid[r][c])

            cnt_z += max(grid[r])

        cnt_y += sum(max(col) for col in cols)

        return cnt_x + cnt_y + cnt_z


sol = Solution()
ret = sol.projectionArea([[2]])
print(ret)
