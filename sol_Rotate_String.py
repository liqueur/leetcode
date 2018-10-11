

class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if not (len(A) == len(B)):
            return False

        if A == '':
            return True

        for i in range(len(A)):
            c = A[1:] + A[0]
            if c == B:
                return True
            else:
                A = c

        return False
