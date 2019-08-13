class Solution:
    # 简单粗暴的方式`
    def mypow1(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        ans = 1
        for i in range(n):
            ans = ans * x
        return ans

    def mypow2(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        ans = 1
        while n:
            if n & 1:
                ans *= x
            x *= x
            n >>= 1
        return ans

    def mypow3(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        return self.fastPow(x, n)

    def fastPow(self, x, n):
        if n == 0: return 1.0
        half = self.fastPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x



if __name__ == "__main__":
    print(Solution().mypow1(2, 10))
    print(Solution().mypow2(2, 7))
    print(Solution().mypow3(2, 9))
