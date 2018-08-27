# coding:utf-8


'''
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        output = []
        for ss in list(s):
            if ss != ' ':
                stack.append(ss)
            else:
                while stack:
                    output.append(stack.pop())
                output.append(ss)

        while stack:
            output.append(stack.pop())
        return ''.join(output)


sol = Solution()
ret = sol.reverseWords("Let's take LeetCode contest")
print(ret)
