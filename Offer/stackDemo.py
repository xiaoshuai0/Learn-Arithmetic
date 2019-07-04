


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char not in dic:
                stack.append(char)
            elif not stack or dic[char] != stack.pop():
                return False
        return not stack

    def isValid2(self, s):
        length = 0
        while True:
            length = len(s)
            s = s.replace('()', '').replace('[]', '').replace('{}', '')
            if length == len(s):
                break
        return len(s) == 0



if __name__ == "__main__":
    print(Solution().isValid("()[]{}"))
    print(Solution().isValid2("()[]{}"))