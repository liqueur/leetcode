# coding:utf-8


'''
1.全部大写
2.全部小写
3.第一个字母大写，其它小写
'''
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        word = [1 if w == w.upper() else 0 for w in word]
        print(word)

        # 1.全部大写
        if sum(word) == len(word):
            return True

        # 2.全部小写
        if sum(word) == 0:
            return True

        # 3.第一个字母大写，其它小写
        if word[0] == 1 and sum(word[1:]) == 0:
            return True

        return False


sol = Solution()
ret = sol.detectCapitalUse('USSAa')
print(ret)
