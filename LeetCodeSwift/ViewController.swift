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
    }

}

