# coding:utf-8


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for ss in s:
            stack.append(ss)

        output = []
        while stack:
            output.append(stack.pop())

        return ''.join(output)


sol = Solution()
ret = sol.reverseString('hello')
print(ret)
