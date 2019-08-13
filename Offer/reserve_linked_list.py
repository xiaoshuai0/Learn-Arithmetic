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
from queue import PriorityQueue


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
        # 遍历一遍节点总数
        dummy = ListNode(0)
        dummy.next = head
        first = head
        length = 0
        while first:
            length += 1
            first = first.next
        # 获取删除节点前的节点数
        length -= n
        first = dummy
        while length > 0:
            length -= 1
            first = first.next
        first.next = first.next.next
        return dummy.next

    def mergeSortLinked(self, head1, head2):
        if head1 is None: return head2
        if head2 is None: return head1
        dummy = ListNode(0)
        cur = dummy

        while head1 and head2:
            if head1.val <= head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
        cur.next = head1 if head1 else head2
        return dummy.next

    def mergeTwoLists(self, l1, l2):
        if l1 is None: return l2
        elif l2 is None: return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def entryNodeForLoop(self, head):
        # dict = set()
        # while head:
        #     if head in dict:
        #         return head
        #     dict.add(head)
        #     head = head.next
        # return None
        meetingNode = self.meetingNode(head)
        if meetingNode is None: return None
        # 得到环中节点的数目
        nodesLoop = 1
        pNode1 = meetingNode
        while pNode1.next != meetingNode:
            pNode1 = pNode1.next
            nodesLoop += 1
        # 先移动pNode1, 次数为环中节点的数目
        pNode1 = head
        for i in range(nodesLoop):
            pNode1 = pNode1.next
        # 在移动pNode1和pNode2
        pNode2 = head
        while pNode1 != pNode2:
            pNode1 = pNode1.next
            pNode2 = pNode2.next
        return pNode1



    def meetingNode(self, node):
        if node is None: return None
        slow = node.next
        if slow is None: return None
        fast = node.next
        while fast and slow:
            if fast == slow:
                return slow
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        return None

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        dummy = ListNode(0)
        p = dummy
        head = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next
        while head:
            val, idx = heapq.heappop(head)
            p.next = ListNode(val)
            p = p.next
            if lists[idx]:
                heapq







if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(3)
    node1.next = node2
    node3 = ListNode(5)
    node2.next = node3
    node4 = ListNode(7)
    node3.next = node4
    node5 = ListNode(9)
    node4.next = node5


    node11 = ListNode(2)
    node21 = ListNode(4)
    node11.next = node21
    node31 = ListNode(6)
    node21.next = node31
    node41 = ListNode(8)
    node31.next = node41

    node12 = ListNode(1)
    node22 = ListNode(3)
    node12.next = node22
    node32 = ListNode(5)
    node22.next = node32
    # head = Solution().reverseList(node1)
    # Solution().printListNode(head)
    # head = Solution().reverseBetween(node1, 2, 4)
    # Solution().printListNode(head)
    # head = Solution().removeNthFromEnd(node1, 1)
    # Solution().printListNode(head)
    # head = Solution().mergeSortLinked(node1, node11)
    # head = Solution().mergeTwoLists(node1, node11)
    # Solution().printListNode(head)
    # loopNode = Solution().entryNodeForLoop(node1)
    # print(loopNode.val)

    head = Solution().mergeKLists([node1, node11, node12])
    Solution().printListNode(head)
