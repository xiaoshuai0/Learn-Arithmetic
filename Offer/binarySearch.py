


class Solution(object):
    # 查找第一个值等于给定值的元素
    def bsearch(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            if nums[mid] > target: high = mid - 1
            elif nums[mid] < target: low = mid + 1
            else:
                if mid == 0 or nums[mid - 1] != target: return mid
                high = mid - 1
        return -1
    # 查找最后一个值等于给顶元素
    def bsearchLast(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                if mid == len(nums) - 1 or nums[mid + 1] != target: return mid
                low = mid + 1
        return -1
#     查找第一个大于等于给定值的元素
    def bsearchFirst(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            if nums[mid] >= target:
                if mid == 0 or nums[mid - 1] < target: return mid
                else:
                    high = mid - 1
            else:
                low = mid + 1
        return -1
#     查找最后一个小于等于给定值的元素
    def bsearchLastSmallOrEqual(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            if nums[mid] > target:
                high = mid - 1
            else:
                if mid == len(nums) - 1 or nums[mid + 1] > target: return mid
                low = mid - 1
        return -1

    # 两数相除
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = (dividend > 0) ^ (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 0
        # 把除数不断左移，直到它大于被除数
        while dividend >= divisor:
            count += 1
            divisor <<= 1
        result = 0
        while count > 0:
            count -= 1
            divisor >>= 1
            if divisor <= dividend:
                result += 1 << count #这里的移位运算是把二进制（第count+1位上的1）转换为十进制
                dividend -= divisor
        if sign: result = -result
        return result if -(1 << 31) <= result <= (1 << 31) - 1 else (1 << 31) - 1


    def searchRange(self, nums, target):
        low, high = 0, 0
        while low <= high:
            mid = low + ((high - low) >> 1)
            if nums[mid] > target: high = mid - 1
            elif nums[mid] < target: low = mid + 1
            





if __name__ == "__main__":
    print(Solution().bsearch([1, 3, 4, 5, 6, 8, 8, 8, 11, 18], 8))
    print(Solution().bsearchLast([1, 3, 4, 5, 6, 8, 8, 8, 11, 18], 8))
    print(Solution().bsearchFirst([3,5, 6, 8, 9, 10], 7))
    print(Solution().bsearchLastSmallOrEqual([3, 5, 6, 8, 9, 10], 7))
    print(Solution().divide(42, 2))






