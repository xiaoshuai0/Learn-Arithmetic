class Solution:

    def quick_sort(self, nums):
        if len(nums) == 0: return []
        left, right, middle = [], [], nums[0]
        for i in range(1, len(nums)):
            if nums[i] < middle:
                left.append(nums[i])
            else:
                right.append(nums[i])
        return self.quick_sort(left) + [middle] + self.quick_sort(right)

    def merge_sort(self, nums):
        if len(nums) <= 1: return nums
        middle = len(nums) // 2
        left = self.merge_sort(nums[:middle])
        right = self.merge_sort(nums[middle:])
        return self.merge_helper(left, right)

    def merge_helper(self, left, right):
        l, r, res = 0, 0, []

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                res.append(left[l])
                l += 1
            else:
                res.append(right[r])
                r += 1
        if l < len(left): res += left[l:]
        if r < len(right): res += right[r:]
        return res
    result = [0] * 8
    def cal8queens(self, row):
        if row == 8:
            self.printQueens()
            return
        for column in range(8):
            if self.isOk(row, column):
                print('row' + str(row) + '       ' + 'column' + str(column))
                self.result[row] = column
                print(self.result)
                self.cal8queens(row + 1)

    def isOk(self, row, column):
        left, right = column - 1, column + 1
        for i in reversed(range(0, row)):
            if self.result[i] == column: return False
            if left >= 0:
                if self.result[i] == left: return False
            if right < 8:
                if self.result[i] == right: return False

            left -= 1
            right += 1
        return True


    def printQueens(self):
        for row in range(8):
            for column in range(8):
                if self.result[row] == column: print("Q ", end='')
                else:print("* ", end="")
            print()
        print()

    maxW = 0
    def f(self, i, cw, items, n, w):
        if cw == w or i == n:
            if cw > self.maxW: self.maxW = cw
            print(self.maxW)
            return

        self.f(i+1, cw, items, n, w)
        if cw + items[i] <= w:
            print('--------' + str(i))
            self.f(i+1, cw + items[i], items, n, w)

    # def isMatch(self, s, p):
    #     """
    #     :type s: str
    #     :type p: str
    #     :rtype: bool
    #     """
    #     # 没有通配符*的匹配方式
    #     # if not p: return not s
    #     # first_match = bool(s) and p[0] in {s[0], '.'}
    #     # return first_match and self.isMatch(s[1:], p[1:])
    #     print(s + '-------' + p)
    #     if not p: return not s
    #     first_match = bool(s) and p[0] in {s[0], '.'}
    #     if len(p) >=2 and p[1] == '*':
    #         return (self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p))
    #     else:
    #         return first_match and self.isMatch(s[1:], p[1:])
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p: return not s
        first_match = bool(s) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])



    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        def backTrack(combination, next_digits):
            if len(next_digits) == 0:
                output.append(combination)
            else:
                for letter in dict[next_digits[0]]:
                    backTrack(combination + letter, next_digits[1:])
        output = []
        if digits:
            backTrack("", digits)
        return output

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def backTrack(s = '', l = 0, r = 0):
            if len(s) == n * 2:
                ans.append(s)
                return
            if l < n:
                backTrack(s + '(', l + 1, r)
            if r < l:
                backTrack(s + ')', l, r + 1)

        backTrack()
        return ans


if __name__ == "__main__":
    # print(Solution().quick_sort([4, 2, 6, 8, 1, 7]))
    # print(Solution().merge_sort([4, 2, 6, 8, 1, 7]))
    # Solution().cal8queens(0)
    Solution().f(0, 0, [11, 22, 33, 45, 43], 5, 100)
    print(Solution().isMatch("aaaaabaccbbccababa", "a*b*.*c*c*.*.*.*c"))
    print(Solution().letterCombinations('23'))
    print(Solution().generateParenthesis(2))
