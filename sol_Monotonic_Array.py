
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if not A:
            return False

        if len(A) == 1:
            return True

        eq = dec = inc = 0

        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                dec += 1
            elif A[i] < A[i + 1]:
                inc += 1
            else:
                eq += 1

        if (eq == len(A) - 1) or (dec and not inc) or (not dec and inc):
            return True

        return False

