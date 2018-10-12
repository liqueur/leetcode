
"""
1, 2, 3, 5

f(1) = 1
f(2) = 2
f(3) = f(1) + f(2) = 3
f(4) = f(3) + f(2) = 5

   *
  **
 ***
****

Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6

dp[i] = min(dp[i- 2] + cost[i - 2], dp[i - 1] + cost[i - 1])

dp[0]
dp[1]
dp[2] = min(dp[0] + cost[0], dp[1] + cost[1])
    = min(0 + 1, 0 + 100)
    = 1
"""


class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0, 0]
        for i in range(2, len(cost) + 1):
            dp.append(min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]))

        return dp[-1]
