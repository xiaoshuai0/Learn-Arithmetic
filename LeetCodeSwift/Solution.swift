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
    /// 3. 无重复字符的最长子串
    func lengthOfLongestSubstring(_ s: String) -> Int {
        let str = Array(s)
        if str.count < 2 {
            return str.count
        } else if str.count == 2 {
            if str[0] == str[1] {
                return 1
            } else {
                return 2
            }
        }
        var dic: [Character: Int] = [:]
        var max_len: Int = 1
        var start: Int = 0
        for i in 0..<str.count {
            let char = str[i]
            if let loc = dic[char] {
                start = max(start, loc + 1)
            }
            dic[char] = i
            max_len = max(max_len, i - start + 1)
        }
        return max_len
    }
    /// 4. 寻找两个有序数组的中位数
    func findMedianSortedArrays(_ nums1: [Int], _ nums2: [Int]) -> Double {
        var (m, n, A, B) = (nums1.count, nums2.count, nums1, nums2)
        
        if m > n {
            (m, n, A, B) = (n, m, B, A)
        }
        
        var (iMin, iMax, halfLen) = (0, m, (m + n + 1) / 2)
        
        while iMin <= iMax {
            let i = (iMin + iMax) / 2
            let j = halfLen - i
            if i < iMax && B[j - 1] > A[i] {
                iMin = i + 1
            } else if i > iMin && A[i - 1] > B[j] {
                iMax = i - 1
            } else {
                var maxLeft = 0
                if i == 0 { maxLeft = B[j - 1] }
                else if j == 0 { maxLeft = A[i - 1] }
                else { maxLeft = max(A[i - 1], B[j - 1]) }
                
                if (m + n) & 1 == 1 { return Double(maxLeft) }
                
                var minRight = 0
                if i == m { minRight = B[j]}
                else if j == n { minRight = A[i] }
                else { minRight = min(B[j], A[i])}
                
                return Double(maxLeft + minRight) / 2.0
            }
        }
        return 0.0
    }
    /// 5.最长回文子串
    func longestPalindrome(_ s: String) -> String {
        var res = ""
        let len = s.count
        for i in 0..<len {
            print(i)
            var temp = longestPalindrome_helper(s, l: i, r: i)
            res = res.count > temp.count ? res : temp
            temp = longestPalindrome_helper(s, l: i, r: (i + 1))
            res = res.count > temp.count ? res : temp
        }
        return res
    }
    
    func longestPalindrome_helper(_ s: String, l: Int, r: Int) -> String {
        let str = Array(s)
        var (left, right) = (l, r)
        while left >= 0 && right < str.count && str[left] == str[right]  {
            left -= 1
            right += 1
        }
        let temp = str[left + 1 ..< right]
        return String(temp)
    }
    
    /// 6. Z 字形变换
    func convert(_ s: String, _ numRows: Int) -> String {
        if numRows == 1 || numRows > s.count { return s }
        var res = Array(repeating: "", count: numRows)
        var (index, step) = (0, 1)
        for x in s {
            var temp = res[index]
            temp = "\(temp)\(x)"
            res[index] = temp
            if index == 0 {
                step = 1
            } else if index == numRows - 1 {
                step = -1
            }
            index += step
        }
        return res.joined()
    }
    /// 7. 整数反转
    func reverse(_ x: Int) -> Int {
        let isNegative = x < 0
        var num = abs(x)
        var res = 0
        let max = (1 << 31) - 1
        
        while num > 0 {
            let temp = num % 10
            if (max / 10 == res && temp > 7) || max / 10 < res {
                return 0
            }
            res = res * 10 + temp
            num = num / 10
        }
        
        return isNegative ? -res : res
    }
    /// 8. 字符串转换整数 (atoi)
    func myAtoi(_ str: String) -> Int {
        let list = Array(str)
        var (i, res, isNegative) = (0, 0, false)
        let max = (1 << 31) - 1
        while i < list.count && list[i] == " "{
            i += 1
        }
        if i < list.count && (list[i] == "-" || list[i] == "+") {
            isNegative = list[i] == "-"
            i += 1
        }
        while i < list.count {
            if let num = Int(String(list[i])) {
                if max / 10 < res || (max / 10 == res && num > 7) {
                    return isNegative ? (-max - 1) : max
                }
                res = res * 10 + num
                i += 1
            } else {
                break
            }
        }
        return isNegative ? -res : res
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
