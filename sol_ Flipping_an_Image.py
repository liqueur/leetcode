
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for r in range(len(A)):
            L, R = 0, len(A[r]) - 1
            while L < R:
                A[r][L], A[r][R] = A[r][R], A[r][L]
                L += 1
                R -= 1

        for r in range(len(A)):
            for c in range(len(A[r])):
                A[r][c] = 1 - A[r][c]

        return A
