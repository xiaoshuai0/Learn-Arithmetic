//
//  Sort.swift
//  LeetCodeSwift
//
//  Created by 赵帅 on 2019/10/17.
//  Copyright © 2019 sun5kong. All rights reserved.
//

import UIKit

extension Array where Element == Int {
    /*
     快排的时间复杂度是O(nlogn), 数组顺序的情况下是O(n²)
     */
    func quickSort() -> [Int] {
        return quickHelper(nums: self)
    }
    
    fileprivate func quickHelper(nums: [Int]) -> [Int]{
        if nums.count == 0 || nums.count == 1 {
            return nums
        }
        
        let partition = nums.last!
        var left: [Int] = [], right: [Int] = []
        for i in 0..<nums.count - 1 {
            if nums[i] < partition {
                left.append(nums[i])
            } else {
                right.append(nums[i])
            }
        }
        return quickHelper(nums: left) + [partition] + quickHelper(nums: right)
    }
    /*
     归并排序
     */
    func mergeSort() -> [Int] {
        return mergeSortHelper(nums: self)
    }
    
    fileprivate func mergeSortHelper(nums: [Int]) -> [Int] {
        if nums.count == 0 || nums.count == 1 {
            return nums
        }
        
        let middle = nums.count / 2
        return merge(nums1: mergeSortHelper(nums: Array(nums[0..<middle])), nums2: mergeSortHelper(nums: Array(nums[middle..<nums.count])))
    }
    
    fileprivate func merge(nums1: [Int], nums2: [Int]) -> [Int] {
        var index1 = 0, index2 = 0
        var res: [Int] = []
        while index1 < nums1.count && index2 < nums2.count {
            if nums1[index1] < nums2[index2] {
                res.append(nums1[index1])
                index1 += 1
            } else {
                res.append(nums2[index2])
                index2 += 1
            }
        }
        if index1 < nums1.count {
            res.append(contentsOf: nums1[index1..<nums1.count])
        }
        if index2 < nums2.count {
            res.append(contentsOf: nums2[index2..<nums2.count])
        }
        return res
    }
    /* 冒泡排序 */
    func bubbleSort() -> [Int] {
        var nums = self
        for i in 0..<nums.count {
            var flag = false
            for j in 0 ..< nums.count - i - 1 {
                if nums[j] > nums[j+1] {
                    (nums[j], nums[j+1]) = (nums[j+1], nums[j])
                    flag = true
                }
            }
            if !flag {
                break
            }
        }
        return nums
    }
    /* 插入*/
    func insertSort() -> [Int] {
        var nums = self
        for i in 1..<nums.count {
            let value = nums[i]
            var j = i - 1
            while j >= 0 {
                if nums[j] > value {
                    nums[j+1] = nums[j]
                } else {
                    break
                }
                j -= 1
            }
            nums[j + 1] = value
        }
        return nums
    }
    
    func selectSort() -> [Int] {
        var nums = self
        for i in 0 ..< nums.count - 1 {
            var min = nums[i], minIndex = i
            for j in i+1 ..< nums.count {
                if nums[j] < min {
                    min = nums[j]
                    minIndex = j
                }
            }
            (nums[i], nums[minIndex]) = (nums[minIndex], nums[i])
        }
        return nums
    }
}
