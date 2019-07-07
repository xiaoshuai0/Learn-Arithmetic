class Solution(object):

    # 冒泡排序时间复杂度 n^2
    def bubbleSort(self, nums):
        flag = False
        for i in range(len(nums)):
            for j in range(0 , len(nums) - i - 1):
                print(j)
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    flag = True
            if not flag:
                break
        return nums
    # 插入排序时间复杂度 n^2
    def insertionSort(self, nums):
        for i in range(1, len(nums)):
            value = nums[i]
            j = i - 1
            while j >= 0:
                if nums[j] > value:
                    nums[j + 1] = nums[j]
                else:
                    break
                j -= 1
            nums[j+1] = value
        return nums

    # 选择排序时间复杂度 n^2
    def selectionSort(self, nums):
        for i in range(0, len(nums) - 1):
            minIndex = i
            for j in range(i + 1, len(nums)):
                if nums[minIndex] > nums[j]:
                    minIndex = j
            nums[minIndex], nums[i] = nums[i], nums[minIndex]
        return nums
    # 归并排序时间复杂度 nlogn
    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums
        num = len(nums) // 2
        left = self.mergeSort(nums[:num])
        right = self.mergeSort(nums[num:])
        return self.merge(left, right)

    def merge(self, left, right):
        r, l = 0, 0
        result = []
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        result += list(left[l:])
        result += list(right[r:])
        return result

    def quickSort(self, nums):
        if len(nums) <= 1: return nums
        mid = nums[0]
        left, right = [], []
        nums.remove(mid)
        for num in nums:
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        return self.quickSort(left) + [mid] + self.quickSort(right)

if __name__ == "__main__":
    # print(Solution().bubbleSort([2,9,3,4,8,3]))
    # print(Solution().insertionSort([2, 9, 3, 4, 8, 3]))
    # print(Solution().selectionSort([2, 9, 3, 4, 8, 3]))
    # print(Solution().mergeSort([2, 9, 3, 4, 8, 3]))
    print(Solution().quickSort([2, 9, 3, 4, 8, 3]))
