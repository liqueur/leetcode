

class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """

        five_cnt = 0
        ten_cnt = 0

        for b in bills:
            if b == 5:
                five_cnt += 1
            elif b == 10 and five_cnt > 0:
                five_cnt -= 1
                ten_cnt += 1
            elif b == 20:
                if five_cnt >= 1 and ten_cnt >= 1:
                    five_cnt -= 1
                    ten_cnt -= 1
                elif five_cnt >= 3:
                    five_cnt -= 3
                else:
                    return False
            else:
                return False

        return True


sol = Solution()
ret = sol.lemonadeChange([5,5,10,10,20])
print(ret)
