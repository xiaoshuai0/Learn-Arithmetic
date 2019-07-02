class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            temp = self.helper(s, i, i)
            if len(temp) > len(res):
                res = temp
            temp = self.helper(s, i, i + 1)
            if len(temp) > len(res):
                res = temp
        return res

    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1: right]



if __name__ == "__main__":
    print(Solution().longestPalindrome("cbbd"))