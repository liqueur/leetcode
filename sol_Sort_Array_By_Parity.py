

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        L, R = 0, len(A) - 1

        while L < R:
            if A[L] % 2 != 0 and A[R] % 2 == 0:
                A[L], A[R] = A[R], A[L]
                L += 1
                R -= 1

            if A[L] % 2 == 0:
                L += 1

            if A[R] % 2 != 0:
                R -= 1

        return A


if __name__ == '__main__':
    sol = Solution()
    sol.sortArrayByParity([3, 1, 2, 4])
