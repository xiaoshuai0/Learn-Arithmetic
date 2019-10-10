//
//  LeetCodeSwiftTests.swift
//  LeetCodeSwiftTests
//
//  Created by 赵帅 on 2019/10/10.
//  Copyright © 2019 sun5kong. All rights reserved.
//

import XCTest
@testable import LeetCodeSwift

class LeetCodeSwiftTests: XCTestCase {
    fileprivate var solution: Solution?
    
    
    override func setUp() {
        // Put setup code here. This method is called before the invocation of each test method in the class.
        //初始化的代码，在测试方法调用之前调用
        super.setUp()
        self.solution = Solution()
    }

    override func tearDown() {
        // Put teardown code here. This method is called after the invocation of each test method in the class.
        // 释放测试用例的资源代码，这个方法会每个测试用例执行后调用
        self.solution = nil
        super.tearDown()
    }

    func testExample() {
        // This is an example of a functional test case.
        // Use XCTAssert and related functions to verify your tests produce the correct results.
//        let res = self.solution?.isValid("[[]") ?? false
        let res = self.solution?.twoSum([2, 7, 11, 15], 9) ?? []
        XCTAssertEqual(res, [0, 1], "无效括号");
    }

    func testPerformanceExample() {
        // This is an example of a performance test case.
        self.measure {
            // Put the code you want to measure the time of here.
        }
    }

}
