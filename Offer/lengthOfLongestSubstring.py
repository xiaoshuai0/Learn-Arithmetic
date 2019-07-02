

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if not s: return 0
        # lookup = set()
        # left, max_len, cur_len = 0, 0, 0
        # for index, item in enumerate(s):
        #     cur_len += 1
        #     while item in lookup:
        #         lookup.remove(s[left])
        #         left += 1
        #         cur_len -= 1
        #     if cur_len > max_len: max_len = cur_len
        #     lookup.add(item)
        # return max_len
        max_length = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if self.allUnique(s, i, j):
                    temp = j - i
                    max_length = temp if temp > max_length else max_length
        return max_length

    def allUnique(self, s, start, end):
        lookup = set()
        for i in range(start, end):
            ch = s[i]
            if ch in lookup: return False
            lookup.add(ch)
        return True

if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("pwwkew"))