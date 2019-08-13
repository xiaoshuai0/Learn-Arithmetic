class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 两个数组有序数组中位数
    def findMedianSortedArrays(self, num1, num2):
        m, n = len(num1), len(num2)
        if m == 0 and n == 0: return
        if m > n:
            m, n, num1, num2 = n, m, num2, num1
        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < imax and num1[i] < num2[j - 1]: imin = i + 1
            elif i > imin and num1[i - 1] > num2[j]: imax = j + 1
            else:
                maxLeft = 0
                if i == 0: maxLeft = num2[j - 1]
                elif j == 0: maxLeft = num1[i - 1]
                else: maxLeft = max(num1[i - 1], num2[j - 1])
                if (m + n) & 1 == 1: return maxLeft

                minRight = 0
                if i == m: minRight = num2[j]
                elif j == n: minRight = num1[i]
                else: minRight = min(num1[i], num2[j])
                return (maxLeft + minRight) / 2.0
        return 0


    #盛最多水的容器
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right, max_area = 0, len(height) - 1, 0
        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
    # 两数相加
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyNode = ListNode(0)
        cur = dummyNode
        carry = 0

        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            sum = num1 + num2 + carry
            carry = sum // 10
            cur.next = ListNode(sum % 10)
            cur = cur.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if carry > 0:
            cur.next = ListNode(carry)
        return dummyNode.next

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            temp = self._helper(s, i, i)
            if len(temp) > len(res):
                res = temp
            temp = self._helper(s, i, i+1)
            if len(temp) > len(res):
                res = temp
        return res

    def _helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isNegative = False
        if x < 0:
            isNeative = True
            x = -x
        res = 0
        while x > 0:
            pop = x % 10
            x = x // 10
            if res > 2**31 / 10  or (res == 2**31 / 10 and pop > 7): return 0
            res = res * 10 + pop
        if isNegative:
            res = -res
        return res
    # 8. 字符串转换整数 (atoi)
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        i, res, neg, over = 0, 0, False, (1 << 31) - 1
        while i < len(str) and str[i] == ' ':
            i += 1
        if i < len(str) and (str[i] == '-' or str[i] == '+'):
            neg = str[i] == '-'
            i += 1
        while i < len(str) and '0' <= str[i] <= '9':
            if over // 10 < res or (res == over // 10 and int(str[i]) > 7):
                return over if not neg else (-over - 1)
            res = res * 10 + int(str[i])
            i += 1
        return res if not neg else -res
    # 回文数
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        print(str(x)[::-1])
        return str(x) == str(x)[::-1]

    def isPalindrome2(self, x):
        """
        :type x: int
        :rtype: bool
        """
        def isVaild(c):
            return c.isalnum()

        if not x or len(x) == 0:  return True
        x = x.lower()
        left, right = 0, len(x) - 1
        while left < right:
            while left < right and not isVaild(x[left]):
                left += 1
            while left < right and not isVaild(x[right]):
                right -= 1
            if x[left] != x[right]: return False
            else:
                left += 1
                right -= 1
        return True

    # 最长公共前缀
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: return ""
        elif len(strs) == 1: return strs[0]
        prefix = ""
        strs.sort()
        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]: prefix += strs[0][i]
            else: break
        return prefix
    # 有效括号
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # length = len(s)
        # while True:
        #     s = s.replace('()', '').replace('[]', '').replace('{}', '')
        #     temp = len(s)
        #     if length == temp: break
        #     length = temp
        # return len(s) == 0
        dic = {'}': '{', ')': '(', ']': '['}
        stack = []
        for ch in s:
            if ch not in dic:
                stack.append(ch)
            elif not stack or stack.pop() != dic[ch]:
                return False
        return len(stack) == 0
    # 合并两个有序列表
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next

    def mergeTwoLists2(self, l1, l2):
        if not l1: return l1
        if not l2: return l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists2(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists2(l1, l2.next)
            return l2
    # 三数之和
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 3: return []
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i - 1]: continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]: left += 1
                    while left < right and nums[right] == nums[right - 1]: right -= 1
                    left += 1
                    right -= 1
                elif sum < 0: left += 1
                else: right -= 1
        return res
    # 最接近的三数之和
    def threeSumClosest(self, nums, target):
        if not nums or len(nums) < 3: return None
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if abs(target - sum) < abs(target - ans):
                    ans = sum
                if sum > target:
                    right -= 1
                elif sum < target:
                    left += 1
                else:
                    return ans
        return ans
    # 删除排序数组中的重复项
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return len(set(nums))

        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1

    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        m, n, carry, res = len(num1) - 1, len(num2) - 1, 0, ""
        while m >= 0 or n >= 0:
            temp1 = ord(num1[m]) - ord('0') if m >= 0 else 0
            temp2 = ord(num2[m]) - ord('0') if m >= 0 else 0
            sum = temp1 + temp2 + carry
            carry = sum // 10
            res = str(sum % 10) + res
            m, n = m - 1, n - 1
        if carry: res = str(carry) + res
        return res



    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0": return  "0"

    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0: return 0
        size = 0
        for i in range(len(nums)):
            if nums[size] != nums[i]:
                size += 1
                nums[size] = nums[i]
        size += 1
        return size


if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([1, 2, 3], []))
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
    print(Solution().longestPalindrome("babad"))
    print(Solution().reverse(-120))
    print(Solution().myAtoi("-91283472332"))
    print(Solution().isPalindrome(121))
    print(Solution().longestCommonPrefix(["","",""]))
    print(Solution().isValid("[]"))
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
    print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
    print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
    print(Solution().addStrings('123', '456'))
    print(Solution().removeDuplicates2([1, 1, 2]))
    print(Solution().isPalindrome2("A man, a plan, a canal: Panama"))

























 #
 # m , n = len(num1), len(num2)
 #        if m > n:
 #            m, n, num1, num2 = n, m, num2, num1
 #
 #        imin, imax, half_len = 0, m, (m + n + 1) // 2
 #        while imin <= imax:
 #            i = (imin + imax) // 2
 #            j = half_len - i
 #            if i < imax and num1[i] < num2[j - 1]: imin = i + 1
 #            if i > imin and num1[i - 1] > num1[j]:
 #                imax = i - 1
 #            else:
 #                maxLeft = 0
 #                if i == 0:
 #                    maxLeft = num2[j - 1]
 #                elif j == 0:
 #                    maxLeft = num1[i - 1]
 #                else:
 #                    maxLeft = min(num1[i - 1], num2[j - 1])
 #                if (m + n) % 2 == 1: return maxLeft
 #
 #                minRight = 0
 #                if i == m:
 #                    minRight = num2[j]
 #                elif j == n:
 #                    minRight = num1[i]
 #                else:
 #                    minRight = min(num1[i], num2[j])
 #
 #                return (maxLeft + minRight) / 2.0
 #        return 0