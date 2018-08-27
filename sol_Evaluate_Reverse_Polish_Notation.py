

"""
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation:
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
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

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        nums = []
        for w in tokens:
            if w in ['+', '-', '*', '/']:
                r = nums.pop(-1)
                l = nums.pop(-1)
                if w == '+':
                    result = l + r
                elif w == '-':
                    result = l - r
                elif w == '*':
                    result = l * r
                else:
                    if l * r < 0:
                        if l < 0:
                            l = -l
                        if r < 0:
                            r = -r

                        result = -(l // r)
                    else:
                        result = l // r
                nums.append(result)
            else:
                v = self.str2int(w)
                nums.append(v)

        return nums[0]


sol = Solution()
ret = sol.evalRPN(["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"])
print(ret)
