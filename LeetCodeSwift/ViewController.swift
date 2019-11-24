//
//  ViewController.swift
//  LeetCodeSwift
//
//  Created by 赵帅 on 2019/10/10.
//  Copyright © 2019 sun5kong. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        let solution = Solution()
        print(solution.longestPalindrome("babad"))
        print(solution.convert("LEETCODEISHIRING", 3))
        print(solution.reverse(-123))
        print(solution.longestCommonPrefix(["flower","alow","blight"]))
        print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
        print(solution.letterCombinations("23"))
        print(solution.fourSum([0, 0, 0, 0], 0))
        print(solution.divide(8, 5))
        print(solution.search([4, 5, 6, 0, 1, 2, 3], 4))
        print(solution.searchRange([1, 1, 2, 2, 3, 3, 4, 4], 2))
        print(solution.searchInsert([1, 3, 5, 6], 7))
        print(solution.myPow(2, 10))
        print(solution.searchMatrix([
          [1,   3,  5,  7],
          [10, 11, 16, 20],
          [23, 30, 34, 50]
        ], 13))
        print(solution.bSearchMatrix([
          [1,   3,  5,  7],
          [10, 11, 16, 20],
          [23, 30, 34, 50]
        ], 13))
//        print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
        print(solution.trap([4,2,3]))
        print(solution.strStr("", "pi"))
        let date = Date().timeIntervalSince1970
        print(solution.longestValidParentheses("())"))
        print(Date().timeIntervalSince1970 - date)
//        print([2, 5, 1, 6, 8, 7, 3].quickSort())
//        print([2, 5, 1, 6, 8, 7, 3].mergeSort())
//        print([2, 5, 1, 6, 8, 7, 3].bubbleSort())
//        print([2, 5, 1, 6, 8, 7, 3].insertSort())
//        print([2, 5, 1, 6, 8, 7, 3].selectSort())
//        print(solution.generateParenthesis(3))
//        print(solution.mySqrt(9))
//
//        // 二分查找
//        print(BSearch.bSearch(nums: [2, 5, 8, 8, 10, 20], target: 20))
//        print(BSearch.bSearchFirst(nums: [2, 5, 8, 8, 8, 8, 8, 10, 20], target: 8))
//        print(BSearch.bSearchLast(nums: [2, 5, 8, 8, 8, 8, 8, 10, 20], target: 8))
    }

}

