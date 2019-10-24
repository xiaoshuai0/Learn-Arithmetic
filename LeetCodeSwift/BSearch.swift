//
//  BSearch.swift
//  LeetCodeSwift
//
//  Created by 赵帅 on 2019/10/23.
//  Copyright © 2019 sun5kong. All rights reserved.
//

import UIKit

class BSearch {
    
    class func bSearch(nums: [Int], target: Int) -> Int? {
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
        return nil
    }
    
    class func bSearchFirst(nums: [Int], target: Int) -> Int? {
        var left = 0, right = nums.count - 1
        while left <= right {
            var mid = left + (right - left) >> 1
            if nums[mid] == target {
                while mid > 0 && nums[mid] == nums[mid - 1] {
                    mid -= 1
                }
                return mid
            } else if nums[mid] > target {
                right = mid - 1
            } else {
                left = mid + 1
            }
        }
        return nil
    }
    
    class func bSearchLast(nums: [Int], target: Int) -> Int? {
        var left = 0, right = nums.count - 1
        while left <= right {
            var mid = left + (right - left) >> 1
            if nums[mid] == target {
                while mid < nums.count - 1 && nums[mid] == nums[mid + 1] {
                    mid += 1
                }
                return mid
            } else if nums[mid] > target {
                right = mid - 1
            } else {
                left = mid + 1
            }
        }
        return nil
    }
    
    class func bSearchFirstGreater(nums: [Int], target: Int) -> Int? {
        var left = 0, right = nums.count - 1
        while left <= right {
            let mid = left + (right - left) >> 1
            if nums[mid] >= target {
                if mid == 0 || nums[mid - 1] < target {
                    return mid
                } else {
                    right = mid - 1
                }
            } else {
                left = mid + 1
            }
        }
        return nil
    }
    
    class func bSearchLastLess(nums: [Int], target: Int) -> Int? {
        var left = 0, right = nums.count - 1
        while left <= right {
            let mid = left + (right - left) >> 1
            if nums[mid] > target {
                right = mid - 1
            } else {
                if mid == nums.count - 1 || nums[mid + 1] > target {
                    return mid
                } else {
                    left = mid + 1
                }
            }
        }
        return nil
    }
}
