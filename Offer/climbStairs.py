
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 方法1: 递归
        # if n == 0 or n == 1:
        #     return 1
        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        # 方法2: 动态规划
        # if n == 1: return 1
        # dp = [0] * (n + 1)
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3,n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[n]
        if n == 1: return 1
        pre, cur = 1, 2
        for i in range(3, n+1):
            pre, cur = cur, pre + cur
        return cur

if __name__ == "__main__":
    print(Solution().climbStairs(3))