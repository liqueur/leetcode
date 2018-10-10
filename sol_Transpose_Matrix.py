class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        nr = len(A)
        nc = len(A[0])

        ret = list()

        for r in range(nr):
            for c in range(nc):
                if c >= len(ret):
                    ret.append([])

                ret[c].append(A[r][c])

        return ret
