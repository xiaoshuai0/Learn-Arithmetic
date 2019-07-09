
import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 方法1: 快速排序, nlog n
        # if len(nums) < k: return None
        # nums = self.quickSort(nums)
        # return nums[-k]

        # 方法2: 小顶堆 nlog k
        # heap = []
        # for num in nums[:k]:
        #     heapq.heappush(heap, num)
        # for num in nums[k:]:
        #     if num > heap[0]:
        #         heapq.heappop(heap)
        #         heapq.heappush(heap, num)
        # return heap[0]
        # 方法3: 快速排序思想
        left = [x for x in nums if x < nums[0]]
        middle = [x for x in nums if x == nums[0]]
        right = [x for x in nums if x > nums[0]]
        f = self.findKthLargest
        if k <= len(right):
            return f(right, k)
        elif k <= len(right) + len(middle):
            return nums[0]
        return f(left, k - len(right) - len(middle))



    def quickSort(self, nums):
        if len(nums) <= 1: return nums
        mid = nums[0]
        left, right = [], []
        nums.remove(mid)
        for num in nums:
            if num > mid:
                right.append(num)
            else:
                left.append(num)
        return self.quickSort(left) + [mid] + self.quickSort(right)




if __name__ == "__main__":
    print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))