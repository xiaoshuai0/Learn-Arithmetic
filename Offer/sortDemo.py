class Solution(object):

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

    def selectionSort(self, nums):
        for i in range(0, len(nums) - 1):
            minIndex = i
            for j in range(i + 1, len(nums)):
                if nums[minIndex] > nums[j]:
                    minIndex = j
            nums[minIndex], nums[i] = nums[i], nums[minIndex]
        return nums

if __name__ == "__main__":
    # print(Solution().bubbleSort([2,9,3,4,8,3]))
    # print(Solution().insertionSort([2, 9, 3, 4, 8, 3]))
    print(Solution().selectionSort([2, 9, 3, 4, 8, 3]))
