
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for index, item in enumerate(nums):
            if target - item in dict:
                return [dict[target - item], index]
            dict[item] = index
        return []

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        时间复杂度：O(\max(m, n))O(max(m,n))，假设 mm 和 nn 分别表示 l1l1 和 l2l2 的长度，上面的算法最多重复 \max(m, n)max(m,n) 次。

        空间复杂度：O(\max(m, n))O(max(m,n))， 新列表的长度最多为 \max(m,n) + 1max(m,n)+1。

        """
        dummyHead = ListNode(0)
        cur = dummyHead
        carry = 0
        while l1 != None or l2 != None:
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
        return dummyHead.next


if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], target=9))
