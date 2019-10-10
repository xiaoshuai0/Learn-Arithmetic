//
//  Solution.swift
//  LeetCodeSwift
//
//  Created by 赵帅 on 2019/10/10.
//  Copyright © 2019 sun5kong. All rights reserved.
//

import UIKit
public class ListNode {
    public var val: Int
    public var next: ListNode?
    public init(_ val: Int) {
        self.val = val
        self.next = nil
    }
}
class Solution {
    /// 1. 两数之和
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var dict: [Int: Int] = [:]
        for (index, value) in nums.enumerated() {
            if dict.keys.contains(target - value) {
                return [dict[target - value]!, index]
            }
            dict[value] = index
        }
        return []
    }
    /// 2. 两数相加
    func addTwoNumbers(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
        var carry: Int = 0
        let dummy: ListNode = ListNode(0)
        var current: ListNode? = dummy
        var l11 = l1
        var l22 = l2
        while l11 != nil || l22 != nil {
            var num1 = 0
            var num2 = 0
            if l11 != nil {
                num1 = l11!.val
                l11 = l11?.next
            }
            if l22 != nil {
                num2 = l22!.val
                l22 = l22?.next
            }
            
            let sum = num1 + num2 + carry
            carry = sum / 10
            current?.next = ListNode(sum % 10)
            current = current?.next
        }
        if carry != 0 {
            current?.next = ListNode(carry)
        }
        return dummy.next
    }
    func lengthOfLongestSubstring(_ s: String) -> Int {
        
    }
    /*20. 有效的括号*/
    func isValid(_ s: String) -> Bool {
//        var stack: [String] = []
//        let pattern: [String: String] = ["]": "[", ")": "(", "}": "{"]
//        for char in s {
//
//            if !pattern.keys.contains(String(char)) {
//                stack.append(String(char))
//            } else if stack.count == 0 || pattern[String(char)] != stack.removeLast() {
//                return false
//            }
//        }
//        return stack.count == 0
        var temp = s
        var lastLength: Int = 0
        while true {
            lastLength = temp.count
            temp = temp.replacingOccurrences(of: "[]", with: "").replacingOccurrences(of: "()", with: "").replacingOccurrences(of: "{}", with: "")
            if temp.count == lastLength {
                break
            }
        }
        return lastLength == 0
    }
}
