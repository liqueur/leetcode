

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict

        count = defaultdict(int)

        for x in s:
            count[x] += 1

        cnt = 0
        for k in count:
            cnt += count[k] // 2

        return cnt * 2 + 1 if len(s) > cnt * 2 else cnt * 2

