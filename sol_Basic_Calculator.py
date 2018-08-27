

"""
Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
"""
class Solution:
    conv1 = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }

    conv2 = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
    }

    order = {
        '+': 0,
        '-': 0,
        '*': 1,
        '/': 1,
        '!': 0,
    }

    def str2int(self, s):
        _sum = i = 0
        _s = list(s)
        neg = None

        if _s[0] == '-':
            neg = _s.pop(0)

        _len = len(_s)

        for j in range(_len):
            _sum += Solution.conv1[_s[_len - j - 1]] * (10 ** i)
            i += 1

        if neg:
            return -_sum

        return _sum

    def int2str(self, val):
        s = ''
        if val == 0:
            return '0'

        _val = val
        if _val < 0:
            _val = -_val

        while _val:
            v = _val % 10
            s = Solution.conv2[v] + s
            _val //= 10

        if val < 0:
            return '-' + s

        return s

    def cal(self, expr):
        word = ''
        opts = []
        nums = []
        _expr = list(expr)
        _expr.append('!')
        ng = False

        for c in _expr:
            if c == ' ':
                if word != '':
                    nums.append(self.str2int(word))
                    word = ''
            elif c in ['+', '-', '*', '/', '!']:
                if word:
                    n = self.str2int(word)
                    if ng:
                        n = -n
                        ng = False
                    nums.append(n)
                    word = ''
                elif c == '-':
                    # 处理负数
                    if not nums:
                        opts.append('+')
                    ng = True
                    continue

                while len(nums) >= 2 and opts and Solution.order[opts[-1]] >= Solution.order[c]:
                    opt = opts.pop(-1)
                    r = nums.pop(-1)
                    l = nums.pop(-1)
                    if opt == '+':
                        val = l + r
                    elif opt == '-':
                        val = l - r
                    elif opt == '*':
                        val = l * r
                    else:
                        val = l // r
                    nums.append(val)

                opts.append(c)
            else:
                word += c

        return nums[0]

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = []
        _s = list(s)
        _s.append(')')
        _s.insert(0, '(')

        for c in _s:
            if c == ')':
                expr = ''
                while words:
                    w = words.pop(-1)

                    if w == '(':
                        result = self.cal(expr)
                        words.append(self.int2str(result))
                        break

                    expr = w + expr

            else:
                words.append(c)

        return self.str2int(words[0])



sol = Solution()
ret = sol.calculate('1+2*-11')
print(ret)