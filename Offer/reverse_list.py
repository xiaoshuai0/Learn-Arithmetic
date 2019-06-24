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

        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p



    def printListNode(self, head):
        current = head
        while current:
            print(current.val)
            current = current.next

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    node3 = ListNode(3)
    node2.next = node3
    node4 = ListNode(4)
    node3.next = node4
    node5 = ListNode(5)
    node4.next = node5
    head = Solution().reverseList(node1)
    Solution().printListNode(head)