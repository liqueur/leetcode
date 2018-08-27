

"""
Input: "3+2*2"
Output: 7

Input: " 3/2 "
Output: 1

Input: " 3+5 / 2 "
Output: 5
"""


class Solution:
    conv = {
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
        _len = len(_s)

        for j in range(_len):
            _sum += Solution.conv[s[_len - j - 1]] * (10 ** i)
            i += 1

        return _sum

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        word = ''
        nums = []
        opts = []
        _s = list(s)
        _s.append('!')
        ng = False

        for c in _s:
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
                    print('c={} word={} nums={} opts={}'.format(c, word, nums, opts))
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

                if c == '!':
                    return nums[0]

                opts.append(c)
            else:
                word += c


sol = Solution()
ret = sol.calculate('-1-1')
print(ret)
