

"""
Example 1:

Input: "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.
Example 2:

Input: "abc"
Output: []
Explanation: We have "a","b" and "c" but no large group.
Example 3:

Input: "abc ddd eeee aa bbb cd"
Output: [[3,5],[6,9],[12,14]]
"""


class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        S += '\n'
        ns = len(S)
        res = list()
        start = end = 0

        for i in range(ns - 1):
            if S[i] == S[i + 1]:
                end = i + 1
            else:
                if end - start + 1 >= 3:
                    res.append([start, end])
                start = end = i + 1

        return res


args = ("abcdddeeeeaabbbcd", )
sol = Solution()
ret = sol.largeGroupPositions(*args)
print(ret)

