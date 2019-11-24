//
//  Practice.swift
//  LeetCodeSwift
//
//  Created by 赵帅 on 2019/11/20.
//  Copyright © 2019 sun5kong. All rights reserved.
//

import UIKit

class Practice {
    /*
     1. 数组在内存是连续, 插入和删除是O(n), 查询是O(1)
     2. 链表不是连续内存, 插入和删除是O(1), 查询是O(n) ,不知道到底有多少数据时
     */
    func reverseList1(_ head: ListNode?) -> ListNode? {
        var pre: ListNode? = nil, cur = head
        while cur != nil {
            (cur!.next, pre, cur) = (pre, cur, cur!.next)
        }
        return cur
    }
    
    func reverseList2(_ head: ListNode?) -> ListNode? {
        if head == nil || head?.next == nil { return head }
        let p = reverseList2(head!.next)
        head!.next!.next = head
        head!.next = nil
        return p
    }
    
    func swapPairs(_ head: ListNode?) -> ListNode? {
        if head == nil || head?.next == nil { return head }
        let next = head!.next!
        head!.next = swapPairs(next.next)
        next.next = head
        return next
    }
    
    func hasCycle(_ head: ListNode?) -> Bool {
//        var nodes = Set<Int>()
//        var node = head
//        while node != nil {
//            if nodes.contains(node!.val) {
//                return true
//            } else {
//                nodes.insert(node!.val)
//                node = node?.next
//            }
//        }
//        return false
        if head == nil || head?.next == nil {
            return false
        }
        var slow = head, fast = head?.next
        while slow?.val != fast?.val {
            if fast == nil || fast?.next == nil {
                return false
            }
            slow = slow?.next
            fast = fast?.next?.next
        }
        return true
    }
    
    func addTwoNumbers(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
        let dummy = ListNode(0)
        var cur: ListNode = dummy, l1 = l1, l2 = l2
        var carry = 0
        while l1 != nil || l2 != nil {
            var num1 = 0, num2 = 0
            if l1 != nil {
                num1 = l1!.val
                l1 = l1!.next
            }
            if l2 != nil {
                num1 = l2!.val
                l2 = l2!.next
            }
            let sum = num1 + num2 + carry
            carry = sum / 10
            cur.next = ListNode(sum % 10)
            cur = cur.next!
        }
        if carry != 0 {
            cur.next = ListNode(carry)
        }
        return dummy.next
    }
    
    
    func isValid(_ s: String) -> Bool {
        var temp = s
        var lastLength = 0
        while true {
            lastLength = temp.count
            temp = temp.replacingOccurrences(of: "[]", with: "").replacingOccurrences(of: "()", with: "").replacingOccurrences(of: "{}", with: "")
            if lastLength == temp.count {
                break
            }
        }
        return lastLength == 0
    }
    
    func isValid2(_ s: String) -> Bool {
        var stack: [String] = []
        let mapping = [")": "(", "]": "[", "}": "{"]
        for char in s {
            if !mapping.keys.contains(String(char)) {
                stack.append(String(char))
            } else if stack.isEmpty || stack.removeLast() != mapping[String(char)]{
                return false
            }
        }
        return stack.isEmpty
    }
}
struct Stack<Element> {
    fileprivate var list: [Element] = []
    
    mutating func push(_ element: Element) {
        list.append(element)
    }
    
    mutating func pop() -> Element {
        return list.popLast()!
    }
    
    func peek() -> Element {
        return list.last!
    }
    
    func size() -> Int {
        return list.count
    }
    
    func isEmpty() -> Bool {
        return list.isEmpty
    }
}

class MyQueue {

    var stackA = Stack<Int>()
    var stackB = Stack<Int>()
    
    func transfer() {
        if stackA.isEmpty() {
            while !stackB.isEmpty() {
                stackA.push(stackB.pop())
            }
        }
    }
    
    init() {
        
    }
    
    /** Push element x to the back of queue. */
    func push(_ x: Int) {
        stackB.push(x)
    }
    
    /** Removes the element from in front of queue and returns that element. */
    func pop() -> Int {
        transfer()
        return stackA.pop()
    }
    
    /** Get the front element. */
    func peek() -> Int {
        transfer()
        return stackA.peek()
    }
    
    /** Returns whether the queue is empty. */
    func empty() -> Bool {
        return stackA.isEmpty() && stackB.isEmpty()
    }
}

struct Queue<Element> {

    fileprivate var list: [Element] = []
    
    init() {
        
    }
    
    /** Push element x to the back of queue. */
    mutating func push(_ x: Element) {
        list.append(x)
    }
    
    /** Removes the element from in front of queue and returns that element. */
    mutating func pop() -> Element {
        return list.removeFirst()
    }
    
    /** Get the front element. */
    func peek() -> Element {
        return list.first!
    }
    
    /** Returns whether the queue is empty. */
    func empty() -> Bool {
        return list.isEmpty
    }
}
class MyStack {

    var queueA = Queue<Int>()
    var queueB = Queue<Int>()
    /** Initialize your data structure here. */
    init() {
        
    }
    
    /** Push element x onto stack. */
    func push(_ x: Int) {
        while !queueA.empty() {
            queueB.push(queueA.pop())
        }
        queueA.push(x)
        while !queueB.empty() {
            queueA.push(queueB.pop())
        }
    }
    
    /** Removes the element on top of the stack and returns that element. */
    func pop() -> Int {
        return queueA.pop()
    }
    
    /** Get the top element. */
    func top() -> Int {
        return queueA.peek()
    }
    
    /** Returns whether the stack is empty. */
    func empty() -> Bool {
        return queueA.empty()
    }
}
