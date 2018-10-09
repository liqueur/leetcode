

class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        matrix = []
        n_row = len(M)
        n_col = len(M[0])
        for row in range(n_row):
            new_row = []
            for col in range(n_col):
                x = 0
                n = 0
                if row - 1 >= 0:
                    # 上
                    x += M[row - 1][col]
                    n += 1
                if row + 1 < n_row:
                    # 下
                    x += M[row + 1][col]
                    n += 1
                if col - 1 >= 0:
                    # 左
                    x += M[row][col - 1]
                    n += 1
                if col + 1 < n_col:
                    # 右
                    x += M[row][col + 1]
                    n += 1
                if row - 1 >= 0 and col - 1 >= 0:
                    # 左上
                    x += M[row - 1][col - 1]
                    n += 1
                if row - 1 >= 0 and col + 1 < n_col:
                    # 右上
                    x += M[row - 1][col + 1]
                    n += 1
                if row + 1 < n_row and col - 1 >= 0:
                    # 左下
                    x += M[row + 1][col - 1]
                    n += 1
                if row + 1 < n_row and col + 1 < n_col:
                    # 右下
                    x += M[row + 1][col + 1]
                    n += 1

                x += M[row][col]
                n += 1

                x //= n
                new_row.append(x)

            matrix.append(new_row)

        return matrix


if __name__ == '__main__':
    ip = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ]

    sol = Solution()
    ret = sol.imageSmoother(ip)

    from pprint import pprint
    pprint(ret)
