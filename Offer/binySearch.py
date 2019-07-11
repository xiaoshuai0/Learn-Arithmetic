

class Solution(object):

    def bsearch(self, nums, target):
        low, high = 0, len(nums)
        while low <= high:
            middle = low + ((high - low) >> 1)
            if nums[middle] == target:
                return True
            elif nums[middle] > target:
                high = middle - 1
            else:
                low = middle + 1
        return False

    def binaySearch(self, nums, target):
        return self.bsearchInternally(nums, 0, len(nums) - 1, target)

    def bsearchInternally(self, nums,low, high, target):
        if low > high: return False
        mid = low + ((high - low) >> 1)
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            high = mid - 1
        else:
            low += 1
        return self.bsearchInternally(nums, low, high, target)

if __name__ == "__main__":
    print(Solution().bsearch([8, 11, 19, 23, 27, 33, 45, 55, 67, 98], 24))
    print(Solution().binaySearch([8, 11, 19, 23, 27, 33, 45, 55, 67, 98], 23))