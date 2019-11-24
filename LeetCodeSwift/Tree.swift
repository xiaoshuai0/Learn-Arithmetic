//
//  Tree.swift
//  LeetCodeSwift
//
//  Created by 赵帅 on 2019/11/21.
//  Copyright © 2019 sun5kong. All rights reserved.
//



public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?
    public init(_ val: Int) {
        self.val = val
        self.left = nil
        self.right = nil
    }
    
    /* 前序*/
    class func preOrder(root: TreeNode?) {
        guard let root = root else { return }
        print(root.val)
        preOrder(root: root.left)
        preOrder(root: root.right)
    }
    /* 中序*/
    class func inOrder(root: TreeNode?) {
        guard let root = root else { return }
        preOrder(root: root.left)
        print(root.val)
        preOrder(root: root.right)
    }
    /* 后序*/
    class func postOrder(root: TreeNode?) {
        guard let root = root else { return }
        preOrder(root: root.left)
        preOrder(root: root.right)
        print(root.val)
    }
    /* 按层遍历*/
    class func floorOrder(root: TreeNode?) {
        guard let root = root else { return }
        var list: [TreeNode] = []
        list.append(root)
        while !list.isEmpty {
            let node = list.removeFirst()
            print("\(node.val)")
            if let left = node.left {
                list.append(left)
            }
            if let right = node.right {
                list.append(right)
            }
        }
    }
    
    class func levelOrder(_ root: TreeNode?) -> [[Int]] {
        guard let root = root else { return []}
        var res: [[Int]] = []
        var list: [TreeNode] = []
        list.append(root)
        while !list.isEmpty {
            let size = list.count
            var li: [Int] = []
            for _ in 0..<size {
                let node = list.removeFirst()
                li.append(node.val)
                if let left = node.left {
                    list.append(left)
                }
                
                if let right = node.right {
                    list.append(right)
                }
            }
            res.append(li)
        }
        return res
    }
    
    class func levelOrder2(_ root: TreeNode?) -> [[Int]] {
        guard let root = root else { return []}
        var res: [[Int]] = []
        
        func helper(_ root: TreeNode, level: Int) {
            if res.count == level {
                res.append([])
            }
            var temp = res[level]
            temp.append(root.val)
            res[level] = temp
            if let left = root.left {
                helper(left, level: level + 1)
            }
            if let right = root.right {
                helper(right, level: level + 1)
            }
        }
        helper(root, level: 0)
        return res
    }
    
    class func maxDepth(_ root: TreeNode?) -> Int {
        if root == nil { return 0 }
        return max(maxDepth(root?.left), maxDepth(root?.right)) + 1
    }
    func deleteNode(_ root: TreeNode?, _ key: Int) -> TreeNode? {
        var p = root            // 删除节点
        var pp: TreeNode?       // 删除节点父节点
        while p != nil && p!.val != key {
            pp = p
            if key > p!.val { p = p!.right }
            else { p = p!.left}
        }
        // 没有找到删除节点
        if p == nil { return root}
        
        // 要删除节点有两个子节点
        if p?.left != nil && p?.right != nil { // 查找右子树最小节点
            var minP = p!.right // 最小节点
            var minPP = p       // 最小节点父节点
            while minP?.left != nil {
                minPP = minP
                minP = minP?.left
            }
            p?.val = minP!.val
            p = minP
            pp = minPP
        }
        
        // 删除节点是叶子节点或者仅有一个子节点
        var child: TreeNode? = nil
        if p?.left != nil { child = p?.left }
        else { child = p?.right }
        
        if pp == nil { return child }
        else if pp!.left?.val == p?.val { pp?.left = child }
        else { pp?.right = child }
        return root
    }
    
}
extension TreeNode: Equatable {
    public static func == (lhs: TreeNode, rhs: TreeNode) -> Bool {
        return lhs.val == rhs.val
    }
    
    
}
class BinarySearchTree {
    var root: TreeNode?
    
    func find(data: Int) -> TreeNode? {
        var node = root
        while node != nil {
            if node!.val == data {
                return node
            } else if node!.val > data {
                node = node!.left
            } else {
                node = node!.right
            }
        }
        return nil
    }
    
    func insert(data: Int) {
        if root == nil {
            root = TreeNode(data)
            return
        }
        var node = root
        while node != nil {
            if data > node!.val {
                if node!.right == nil {
                    node?.right = TreeNode(data)
                    return
                }
                node = node!.left
            } else {
                if node!.left == nil {
                    node!.left = TreeNode(data)
                    return
                }
                node = node!.left
            }
        }
    }
    /*
        1. 删除节点是叶子节点只需将父节点的左子树或右子树置为nil
        2. 删除节点只有左子树或者右子树, 父节点指向要删除节点的子树
        3. 删除节点有两个子节点,
     */
    func delete(data: Int) {
        var p = root
        var pp: TreeNode? = nil
        while p != nil && p!.val != data {
            pp = p
            if data > p!.val {
                p = p!.right
            } else {
                p = p!.left
            }
        }
        if p == nil { return }
        if p?.left != nil && p?.right != nil {
            var minP = p?.right
            var minPP = p
            while minP?.left != nil {
                minPP = minP
                minP = minP!.left
            }
            p?.val = minP!.val
            p = minP
            pp = minPP
        }
        
        var child: TreeNode? = nil
        if p?.left != nil {
            child = p!.left
        } else if p?.right != nil {
            child = p?.right
        }
        if pp == nil {
            root = child
        } else if pp?.left == p {
            pp?.left = child
        } else {
            pp?.right = child
        }
    }
    
    
}
