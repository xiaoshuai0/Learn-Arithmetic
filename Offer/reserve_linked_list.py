# Reverse a singly linked list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL


# class Solution {
# func reverseList(_ head: ListNode
#
# ?) -> ListNode? {
#     var
# temp: ListNode?
# var
# first = head
#
# while first != nil {
# let second = first!.next
#
# first!.next = temp
# temp = first
# first = second
# }
# return temp
# }
# }
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # pre, current = None, head
        # while current:
        #     current.next, pre, current = pre, current, current.next
        # return pre

        if head == None or head.next == None: return head
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node

        # pre, current = None, head
        # while current:
        #     temp = current.next
        #     current.next = pre
        #     pre = current
        #     current = temp
        # return pre


    def printListNode(self, head):
        current = head
        while current:
            print(current.val)
            current = current.next
    """
    反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

    说明:
    1 ≤ m ≤ n ≤ 链表长度。

    示例:

    输入: 1->2->3->4->5->NULL, m = 2, n = 4
    输出: 1->4->3->2->5->NULL
    """
    def reverseBetween(self, head, m, n):
        dummyHead = ListNode(0)
        dummyHead.next = head
        pre = dummyHead

        for i in range(m - 1):
            pre = pre.next
        cur = pre.next
        for i in range(m, n):
            temp = cur.next
            cur.next = temp.next
            temp.next = pre.next
            pre.next = temp
        return dummyHead.next

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # dummy = ListNode(0)
        # dummy.next = head
        # pre, fast = dummy, dummy
        # for i in range(1, n + 1):
        #     fast = fast.next
        #
        # while fast.next:
        #     pre = pre.next
        #     fast = fast.next
        # pre.next = pre.next.next
        # return dummy.next
        dummy = ListNode(0)
        dummy.next = head
        first = head
        length = 0
        while first:
            length += 1
            first = first.next

        length -= n
        first = dummy
        while length > 0:
            length -= 1
            first = first.next
        first.next = first.next.next
        return dummy.next


if __name__ == "__main__":
    node1 = ListNode(1)
    # node2 = ListNode(2)
    # node1.next = node2
    # node3 = ListNode(3)
    # node2.next = node3
    # node4 = ListNode(4)
    # node3.next = node4
    # node5 = ListNode(5)
    # node4.next = node5
    # head = Solution().reverseList(node1)
    # Solution().printListNode(head)
    # head = Solution().reverseBetween(node1, 2, 4)
    # Solution().printListNode(head)
    head = Solution().removeNthFromEnd(node1, 1)
    Solution().printListNode(head)
