

class Solution(object):
    def dfs(self, S, i, string, container):
        if i == len(S):
            container.append(string)
            return

        if S[i].isdigit():
            self.dfs(S, i + 1, string + S[i], container)
        else:
            self.dfs(S, i + 1, string + S[i].upper(), container)
            self.dfs(S, i + 1, string + S[i].lower(), container)

    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """

        container = list()
        self.dfs(S, 0, '', container)
        return container


if __name__ == '__main__':
    sol = Solution()
    ret = sol.letterCasePermutation('a1b2')
    print(ret)
