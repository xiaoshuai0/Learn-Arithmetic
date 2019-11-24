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
    /// 9. 回文数
    func isPalindrome(_ x: Int) -> Bool {
        if x < 0 {
            return false
        }
        
        let list = Array(String(x))
        var (left, right) = (0, list.count - 1)
        while left <= right {
            if list[left] != list[right] {
                return false
            }
            left += 1
            right -= 1
        }
        return true
    }
    /// 11. 盛最多水的容器
    func maxArea(_ height: [Int]) -> Int {
    
        if height.count < 2 {
            return 0
        }
        var max_area = 0
        var (left, right) = (0, height.count - 1)
        while left < right {
            let area = (height[left] > height[right] ? height[right] : height[left]) * (right - left)
            max_area = max(area, max_area)
            if height[left] > height[right] {
                right -= 1
            } else {
                left += 1
            }
        }
        return max_area
    }
    /// 12. 整数转罗马数字
    func intToRoman(_ num: Int) -> String {
        let I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        let X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        let C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        let M = ["", "M", "MM", "MMM"]
        return "\(M[num / 1000])\(C[(num % 1000) / 100])\(X[(num % 100) / 10])\(I[num % 10])"
    }
    /// 13. 罗马数字转整数
    func romanToInt(_ s: String) -> Int {
        let roman = ["M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1]
        var res = 0
        let str = Array(s)
        for i in 0..<str.count - 1 {
            guard let cur = roman[String(str[i])], let last = roman[String(str[i + 1])] else {
                return 0
            }
            if cur < last  {
                res -= cur
            } else {
                res += cur
            }
        }
        return res + (roman[String(str[str.count - 1])] ?? 0)
    }
    
    /// 14. 最长公共前缀
    func longestCommonPrefix(_ strs: [String]) -> String {
        if strs.count == 0 {
            return ""
        } else if strs.count == 1 {
            return strs[0]
        }
        var temp = strs
        temp.sort()
        
        var end = 0
        guard let first = temp.first, let last = temp.last else {
            return ""
        }
        let firstList = Array(first)
        let lastList = Array(last)
        while end < first.count {
            if firstList[end] == lastList[end] {
                end += 1
            } else {
                break
            }
        }
        return String(firstList[0..<end])
    }
    /// 15. 三数之和
    func threeSum(_ nums: [Int]) -> [[Int]] {
        if nums.count < 3 {
            return []
        }
        var res: [[Int]] = []
        let nums = nums.sorted()
        for (index, value) in nums.enumerated() {
            if value > 0 { break }
            if index > 0 && nums[index] == nums[index - 1] { continue }
            var (left, right) = (index + 1, nums.count - 1)
            while left < right {
                let sum = value + nums[left] + nums[right]
                if sum == 0 {
                    res.append([value, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right && nums[left] == nums[left - 1] {
                        left += 1
                    }
                    while left < right && nums[right] == nums[right + 1] {
                        right -= 1
                    }
                } else if sum < 0 {
                    left += 1
                } else {
                    right -= 1
                }
            }
        }
        return res
    }
    /// 16. 最接近的三数之和
    func threeSumClosest(_ nums: [Int], _ target: Int) -> Int {
        if nums.count < 3 { return 0 }
        
        let nums = nums.sorted()
        var res: Int = nums[0] + nums[1] + nums[2]
        
        for (index, value) in nums.enumerated() {
            if index > 0 && nums[index] == nums[index - 1] { continue }
            var (left, right) = (index + 1, nums.count - 1)
            while left < right {
                let sum = value + nums[left] + nums[right]
                if abs(target - sum) < abs(target - res) {
                    res = sum
                }
                if sum > res {
                    left += 1
                } else if sum < res {
                    right -= 1
                } else {
                    return res
                }
            }
        }
        return res
    }
    /// 17. 电话号码的字母组合
    func letterCombinations(_ digits: String) -> [String] {
          var combinations = [String](), combination = ""
          
          dfs(createBoard(), &combinations, &combination, Array(digits), 0)
          
          return combinations
      }
      
      fileprivate func createBoard() -> [String] {
          var res = [String]()
    
          res.append("")
          res.append("")
          res.append("abc")
          res.append("def")
          res.append("ghi")
          res.append("jkl")
          res.append("mno")
          res.append("pqrs")
          res.append("tuv")
          res.append("wxyz")
    
          return res
      }
      
      fileprivate func dfs(_ board: [String], _ combinations: inout [String], _ combination: inout String, _ digits: [Character], _ index: Int) {
          if digits.count == index {
              if combination != "" {
                  combinations.append(String(combination))
              }
              
              return
          }
          
          let digitStr = board[Int(String(digits[index]))!]
          
          for digitChar in digitStr {
              combination.append(digitChar)
              dfs(board, &combinations, &combination, digits, index + 1)
              combination.removeLast()
          }
    }
    /// 18. 四数之和
    func fourSum(_ nums: [Int], _ target: Int) -> [[Int]] {
        if nums.count < 4 { return [] }
        let nums = nums.sorted()
        var res: [[Int]] = []
        for index in 0 ..< nums.count - 1 {
            if index != 0 && nums[index] == nums[index - 1] { continue }
            for index_two in index + 1 ..< nums.count {
                if index_two != index + 1 && nums[index_two] == nums[index_two - 1] { continue }
                var left = index_two + 1, right = nums.count - 1
                while left < right {
                    let sum = nums[index] + nums[index_two] + nums[left] + nums[right]
                    if sum == target {
                        res.append([nums[index], nums[index_two], nums[left], nums[right]])
                        left += 1; right -= 1
                        while left < right && nums[left] == nums[left - 1] {
                            left += 1
                        }
                        while left < right && nums[right] == nums[right + 1] {
                            right -= 1
                        }
                    } else if sum < target {
                        left += 1
                    } else {
                        right -= 1
                    }
                }
            }
        }
        return res
    }
    /// 19. 删除链表的倒数第N个节点
    func removeNthFromEnd(_ head: ListNode?, _ n: Int) -> ListNode? {
        let dummy = ListNode(0)
        dummy.next = head
        
        var pre: ListNode? = dummy
        var fast: ListNode? = dummy
        for _ in 1...n {
            fast = fast?.next
        }
        while fast != nil && fast!.next != nil {
            fast = fast?.next
            pre = pre?.next
        }
        pre?.next = pre?.next?.next
        return dummy.next
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
    /// 21. 合并两个有序链表
    func mergeTwoLists(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
        let dummy = ListNode(0)
        var current: ListNode? = dummy
        var l1 = l1, l2 = l2
        while l1 != nil && l2 != nil {
            if l1!.val < l2!.val {
                current?.next = l1
                l1 = l1?.next
            } else {
                current?.next = l2
                l2 = l2?.next
            }
            current = current?.next
            
        }
        if l1 != nil {
            current?.next = l1
        } else {
            current?.next = l2
        }
        return dummy.next
    }
    
    /// 22. 括号生成
    func generateParenthesis(_ n: Int) -> [String] {
        var res: [String] = []
        generateParenthesis_helper(n: n, str: "", left: 0, right: 0, res: &res)
        return res
    }
    
    fileprivate func generateParenthesis_helper(n: Int, str: String, left: Int = 0, right: Int, res: inout [String]) {
        if str.count == n * 2 {
            res.append(str)
            return
        }
        
        if left < n {
            generateParenthesis_helper(n: n, str: "\(str)(", left: left + 1, right: right, res: &res)
        }
        
        if right < left {
            generateParenthesis_helper(n: n, str: "\(str))", left: left, right: right + 1, res: &res)
        }
    }
    
    /// 23. 合并K个排序链表
    func mergeKLists(_ lists: [ListNode?]) -> ListNode? {
        var lists: [ListNode?] = lists
        var count = lists.count, interval = 1
        while interval < count {
            for i in stride(from: 0, to: count - interval, by: interval * 2) {
                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
            }
            interval *= 2
        }
        return count > 0 ? lists[0] : nil
    }
    
    /// 24. 两两交换链表中的节点
    func swapPairs(_ head: ListNode?) -> ListNode? {
        if head == nil || head?.next == nil {
            return head
        }
        let next = head!.next
        head?.next = swapPairs(next?.next)
        next?.next = head
        return next
    }
    
    /// 25. K 个一组翻转链表
//    func reverseKGroup(_ head: ListNode?, _ k: Int) -> ListNode? {
//
//    }
    /// 26. 删除排序数组中的重复项
    func removeDuplicates(_ nums: inout [Int]) -> Int {
       
        var start = 0
        for index in 1..<nums.count {
            if nums[index] != nums[start] {
                start += 1
            }
            nums[index] = nums[start]
        }
        return start + 1
    }
    
    
    /// 28. 实现 strStr()
    func strStr(_ haystack: String, _ needle: String) -> Int {
        if haystack == needle {
            return 0
        }
        if haystack.count == 0 || haystack.count < needle.count {
            return -1
        }
        for i in 0..<(haystack.count - needle.count + 1) {
            let subString = String(haystack[haystack.index(haystack.startIndex, offsetBy: i)..<haystack.index(haystack.startIndex, offsetBy: i + needle.count)])
            if subString == needle {
                return i
            }
        }
        return -1
    }
    /// 29. 两数相除
    func divide(_ dividend: Int, _ divisor: Int) -> Int {
        var sign = false
        if (divisor > 0 && dividend > 0) || (divisor < 0 && dividend < 0){
            sign = true
        }
        var dividend = abs(dividend)
        var divisor = abs(divisor)
        var count = 0
        while dividend >= divisor {
            count += 1
            divisor <<= 1
        }
        var res = 0
        while count > 0 {
            count -= 1
            divisor >>= 1
            if divisor <= dividend {
                res += 1 << count
                dividend -= divisor
            }
        }
        if !sign {
            res = -res
        }
        return res
    }
    /// 32. 最长有效括号
    func longestValidParentheses(_ s: String) -> Int {
//        if s.count < 2 {
//            return 0
//        }
//        var maxLength = 0
//        for i in 0..<s.count {
//            for j in stride(from: i + 2, through: s.count, by: 2) {
//                if isValidParentheses(s: String(s[s.index(s.startIndex, offsetBy: i)..<s.index(s.startIndex, offsetBy: j)])) {
//                    maxLength = max(maxLength, j - i)
//                }
//            }
//        }
//        return maxLength
        var maxLength = 0
        var stack: [Int] = []
        stack.append(-1)
        for (i, value) in s.enumerated() {
            if value == "(" {
                stack.append(i)
            } else {
                stack.removeLast()
                if stack.isEmpty {
                    stack.append(i)
                } else {
                    maxLength = max(maxLength, i - stack.last!)
                }
            }
        }
        return maxLength
    }
    fileprivate func isValidParentheses(s: String) -> Bool {
        var stack: [String] = []
        for (_, value) in s.enumerated() {
            if value == "(" {
                stack.append("(")
            } else if !stack.isEmpty && value == ")" {
                stack.removeLast()
            } else {
                return false
            }
        }
        return stack.isEmpty
    }

    /// 33. 搜索旋转排序数组
    func search(_ nums: [Int], _ target: Int) -> Int {
        var start = 0, end = nums.count - 1
        while start < end {
            let mid = start + (end - start) >> 1
            if nums[mid] > nums[end] {
                start = mid + 1
            } else {
                end = mid
            }
        }
        let offSet = start
        start = 0
        end = nums.count - 1
        while start <= end {
            let mid = start + (end - start) >> 1
            let mid_change = (mid + offSet) % nums.count
            if target == nums[mid_change] {
                return mid_change
            } else if target < nums[mid_change] {
                end = mid - 1
            } else {
                start = mid + 1
            }
        }
        return -1
    }
    
    /// 34. 在排序数组中查找元素的第一个和最后一个位置
    func searchRange(_ nums: [Int], _ target: Int) -> [Int] {
//        var start = 0, end = nums.count - 1
//        while start <= end {
//            let mid = start + (end - start) >> 1
//            if nums[mid] == target {
//                var left = mid, right = mid
//                while left > 0 && nums[left] == nums[left - 1] {
//                    left -= 1
//                }
//                while right < nums.count - 1 && nums[right] == nums[right + 1] {
//                    right += 1
//                }
//                return [left, right]
//            } else if nums[mid] > target {
//                end = mid - 1
//            } else {
//                start = mid + 1
//            }
//        }
//        return [-1, -1]
        let leftIndex = extremeInsertionIndex(nums, target: target, left: true)
        if leftIndex == nums.count || nums[leftIndex] != target {
            return [-1, -1]
        }
        let rightIndex = extremeInsertionIndex(nums, target: target)
        return [leftIndex, rightIndex]
    }
    
    func extremeInsertionIndex(_ nums: [Int], target: Int, left: Bool = false) -> Int{
        var lo: Int = 0, high: Int = nums.count
        
        while lo < high {
            let mid = lo + (high - lo) >> 1
            if nums[mid] > target || (left && nums[mid] == target) {
                high = mid
            } else {
                lo = mid + 1
            }
        }
        return lo
    }
    
    /// 35. 搜索插入位置
    func searchInsert(_ nums: [Int], _ target: Int) -> Int {
        var left = 0, right = nums.count - 1
        while left <= right {
            let mid = left + (right - left) >> 1
            if nums[mid] == target {
                return mid
            } else if nums[mid] > target {
                right = mid - 1
            } else {
                left = mid + 1
            }
        }
        return left
    }
    /// 42. 接雨水
    func trap(_ height: [Int]) -> Int {
        if height.count <= 1 {
            return 0
        }
        var max = height[0], maxIndex = 0, res = 0
        // 获取到最大值所在的下标
        for (index, value) in height.enumerated() {
            if value >= max {
                max = value
                maxIndex = index
            }
        }
        // 获取最大值左边雨量
        max = height[0]
        for i in 0..<maxIndex {
            if height[i] < max {
                res += max - height[i]
            } else {
                max = height[i]
            }
        }
        // 获取最大值右边的雨量
        max = height[height.count - 1]
        for i in stride(from: height.count - 1, to: maxIndex, by: -1) {
            if height[i] < max {
                res += max - height[i]
            } else {
                max = height[i]
            }
        }
        return res
    }
    
    /// 50.Pow(x, n)
    func myPow(_ x: Double, _ n: Int) -> Double {
        var x = x, n = n
        if n < 0 {
            n = -n
            x = 1 / x
        }
        var res: Double = 1
        
        // 方法1:
//        for _ in 0..<n {
//            res *= x
//        }
//        return res
        while n > 0 {
            if n & 1 == 1 {
                res *= x
            }
            x *= x
            print("x: \(x) res: \(res) count: \(n)")
            n = n >> 1
        }
        return res
//        return fastPow(x: x, n: n)
    }
    
    func fastPow(x: Double, n: Int) -> Double {
        if n == 0 {
            return 1.0
        }
        let half = fastPow(x: x, n: n / 2)
        if n & 1 == 0 {
            return half * half
        } else {
            return half * half * x
        }
    }
    func mySqrt(_ x: Int) -> Int {
        var low = 0, high = x, mid = x / 2
        while low <= high && mid * mid != x  {
            if mid * mid < x {
                low = mid + 1
            } else {
                high = mid - 1
            }
            mid = low + ((high - low) >> 1)
        }
        return mid
    }
    /// 74. 搜索二维矩阵
    func searchMatrix(_ matrix: [[Int]], _ target: Int) -> Bool {
        guard matrix.count > 0, var col = matrix.first?.count else {
            return false
        }
        col -= 1
        var row = 0
        while col >= 0 && row < matrix.count {
            if matrix[row][col] == target {
                return true
            } else if matrix[row][col] > target {
                col -= 1
            } else {
                row += 1
            }
        }
        return false
    }
    
    func bSearchMatrix(_ matrix: [[Int]], _ target: Int) -> Bool {
        guard matrix.count > 0, let col = matrix.first?.count else {
            return false
        }
        var left = 0, right = matrix.count * col - 1
        while left <= right {
            let mid = left + (right - left) >> 1
            let element = matrix[mid / col][mid % col]
            if element == target {
                return true
            } else if element > target {
                right = mid - 1
            } else {
                left = mid + 1
            }
        }
        return false
    }
}
