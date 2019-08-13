class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        if l1: current.next = l1
        if l2: current.next = l2
        return dummy.next

    def mergeTwoLists2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None: return l2
        elif l2 is None: return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def mergeKLists1(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        node_list = []
        dummy = ListNode(0)
        cur = dummy
        for head in lists:
            while head:
                node_list.append(head.val)
                head = head.next
        node_list = sorted(node_list)
        for value in node_list:
            cur.next = ListNode(value)
            cur = cur.next
        return dummy.next

    def mergeKLists2(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0: return None
        elif len(lists) == 0: return lists[0]
        else:
            dummy = ListNode(0)
            dummy.next = lists[0]
            for i in range(1, len(lists)):
                dummy.next = self.mergeTwoLists(dummy.next, lists[i])
            return dummy

    def mergeKLists3(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        dummy = ListNode(0)
        cur = dummy
        head = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next
        while head:
            val, idx = heapq.heappop(head)
            cur.next = ListNode(val)
            cur = cur.next
            if lists[idx]:
                heapq.heappush(head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummy.next


    def mergeKLists3(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists

    def swapPairs1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None: return head
        next = head.next
        head.next = self.swapPairs(next.next)
        next.next = head
        return next
    def swapPairs2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = ListNode(0)
        pre.next = head
        temp = pre
        while temp.next != None and temp.next.next != None:
            start = temp.next
            end = temp.next.next
            temp.next = end
            start.next = end.next
            end.next = start
            temp = start
        return pre.next

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
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

        if carry > 0: cur.next = ListNode(carry)
        return dummyHead.next

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        dummyHead.next = head
        slow, fast = dummyHead, dummyHead
        for i in range(1, n + 1):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return slow

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # dummyHead = ListNode(0)
        # cur = dummyHead
        # while l1 != None and l2 != None
        #     if l1.val <= l2.val:
        #         cur.next = l1
        #         l1 = l1.next
        #     else:
        #         cur.next = l2
        #         l2 = l2.next
        #     cur = cur.next
        # if l1: cur.next = l1
        # if l2: cur.next = l2
        # return dummyHead.next
        if l1 is None: return l2
        if l2 is None: return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # pre, cur = None, head
        # while cur:
        #     cur.next, pre, cur = pre, cur, cur.next
        # return pre

        if head is None or head.next is None: return head

        newHead = self.reverseList(head.next)

        next = head.next
        next.next = head
        head = None
        return newHead

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
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

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if head is None or head.next is None: return head
        #
        # next = head.next
        # head.next = self.swapPairs(next.next)
        # next.next = head
        # return next

        dummyHead = ListNode(0)
        dummyHead.next = head
        temp = dummyHead
        while temp.next and temp.next.next:
            start, end = temp.next, temp.next.next
            start.next = end.next
            end.next = start
            temp.next = end
            temp = start
        return dummyHead.next

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        temp, count = head, 0
        while count < k and temp is not None:
            temp = temp.next
            count += 1
        if temp is None: return head

        t2 = temp.next
        temp.next = None

        newHead = self.reverseList(head)
        newTemp = self.reverseKGroup(t2, k)
        head.next = newTemp

        return newHead

    def water_volume(self, arr_list):
        """
        返回积水量
        :param arr_list: 台阶数组
        :return: 返回积水量
        """
        arr_length= len(arr_list)
        arr_max = 0
        arr_max_pos = 0
        for i in range(arr_length):
            if arr_max < arr_list[i]:
                arr_max = arr_list[i]
                arr_max_pos = i

        arr_max_left = 0
        arr_max_right = 0
        volumes = 0

        for i in range(0, arr_max_pos):
            if arr_max_left < arr_list[i]:
                arr_max_left = arr_list[i]
            else:
                volumes += (arr_max_left - arr_list[i])
        for i in range(arr_length - 1, arr_max_pos, -1):
            if arr_max_right < arr_list[i]:
                arr_max_right = arr_list[i]
            else:
                volumes += (arr_max_right - arr_list[i])
        return volumes

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None: return head
        if not head.next: return head

        count = 1
        temp = head
        while temp.next:
            count += 1
            temp = temp.next
        temp.next = head
        temp = head
        for i in range(count - k % count - 1):
            temp = temp.next
        head = temp.next
        temp.next = None
        return head

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return head
        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None: return head
        dummyHead = ListNode(0)
        dummyHead.next = head
        slow = dummyHead
        fast = head
        while fast:
            while fast.next and slow.next.val == fast.next.val:
                fast = fast.next
            if slow.next == fast:
                slow = fast
            else:
                slow.next = fast.next
            fast = fast.next
        return dummyHead.next
if __name__ == "__main__":
    solution = Solution()
    node1 = ListNode(1)
    node1.next = ListNode(4)
    node1.next.next = ListNode(5)

    node2 = ListNode(1)
    node2.next = ListNode(3)
    node2.next.next = ListNode(4)

    node3 = ListNode(2)
    node3.next = ListNode(6)

    solution.mergeKLists3([node1, node2, node3])
    head = solution.reverseList(node1)
    print(head)
    print(solution.water_volume([0,1,0,2,1,0,1,3,2,1,2,1]))
