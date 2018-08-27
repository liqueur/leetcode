

class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        str2int = {
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

        int2str = {
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

        val1 = val2 = 0
        i1 = i2 = 0

        _num1 = list(num1)
        _num2 = list(num2)

        while _num1:
            val1 += str2int[_num1.pop(-1)] * (10 ** i1)
            i1 += 1

        while _num2:
            val2 += str2int[_num2.pop(-1)] * (10 ** i2)
            i2 += 1

        mul = val1 * val2
        _mul = ''

        while mul:
            _mul = int2str[mul % 10] + _mul
            mul //= 10

        if _mul == '':
            _mul = '0'

        return _mul
