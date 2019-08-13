class Solution(object):
    def containsDuplicate1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))

    def containsDuplicate1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict = {}
        for item in nums:
            if item in dict:
                return True
            dict[item] = "-1"
        return False

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = set()
        for i in range(len(nums)):
            if nums[i] in dic:
                return True
            dic.add(nums[i])
            if len(dic) > k:
                dic.remove(nums[i - k])
        return False

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        for i in range(len(nums)):
            temp = i - k if i >= k else 0
            for j in range(temp, i):
                if abs(nums[i] - nums[j]) <= t: return True
        return False






if __name__ == "__main__":
    solution = Solution()
    print(solution.containsNearbyDuplicate([1,0,1,1], 1))
    print(solution.containsNearbyAlmostDuplicate([2, 2], 3, 0))