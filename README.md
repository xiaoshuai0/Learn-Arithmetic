# Learn-Arithmetic
### 队列
> FIFO First In First Out

```
struct Queue<T> {
    
    private var items = [T]()
    
    /** 队列的头元素*/
    var front: T? {
        return items.first
    }
    /** 队列是否为空*/
    var isEmpty: Bool {
        return front == nil
    }
    /** 队列包大小*/
    var size: Int {
        return items.count
    }
    /** 队列的尾部插入*/
    mutating func enqueue(item: T) {
        items.append(item)
    }
    /** 获取第一个元素*/
    mutating func dequeue() -> T? {
        if !isEmpty {
            return items.removeFirst()
        }
        return nil
    }
}
var queue = Queue<Int>()
queue.isEmpty
queue.size
queue.front
queue.enqueue(item: 2)
queue.enqueue(item: 3)
queue.enqueue(item: 5)
queue.isEmpty
queue.size
queue.front
var front: Int? = queue.dequeue()
front = queue.dequeue()
front = queue.dequeue()
front = queue.dequeue()
```
####击鼓传花的规则
* 原游戏规则:
    * 班级中玩一个游戏, 所有学生围成一圈, 从某位同学手里开始向旁边的同学传一束花.
    * 这个时候某个人(比如班长), 在击鼓, 鼓声停下的一颗, 花落在谁手里, 谁就出来表演节目.
* 修改游戏规则:
    * 我们来修改一下这个游戏规则.
    * 几个朋友一起玩一个游戏, 围成一圈, 开始数数, 数到某个数字的人自动淘汰.
    * 最后剩下的这个人会获得胜利, 请问最后剩下的是原来在哪一个位置上的人?

####击鼓传花的实现
```
func passGame(names: [String], num: Int) -> Int {
    
    var queue = Queue<String>()
    for name in names {
        queue.enqueue(item: name)
    }
    
    while queue.size > 1 {
        for _ in 0..<num {
            queue.enqueue(item: queue.dequeue()!)
        }
        queue.dequeue()
    }
    guard let name = queue.dequeue() else {
        return 0
    }
    print(name)
    return names.index(of: name) ?? 0
}


var names = ["John", "Jack", "Camila", "Ingrid", "Carl"];

passGame(names: names, num: 4)
```

### 栈的实现
>First In Last Out
 
```
struct Stack<T> {
    
    
    fileprivate var statckArray = [T]()
    
    public var count:Int {
        return statckArray.count
    }
    
    public var isEmpty: Bool {
        return statckArray.isEmpty
    }
    
    public var top: T? {
        if statckArray.isEmpty {
            return nil
        } else {
            return statckArray.last
        }
    }
    
    public mutating func push(_ element: T) {
        statckArray.append(element)
    }
    
    public mutating func pop() -> T? {
        if isEmpty {
            return nil
        } else {
            return statckArray.removeLast()
        }
    }
    
    public func printAllElements() {
        guard count > 0 else {
            print("stack is empty")
            return
        }
        
        for (index, element) in statckArray.enumerated() {
            print("[\(index)]: \(element)")
        }
    }
}


var stack = Stack.init(statckArray: [])
stack.printAllElements()
stack.isEmpty

stack.push(2)
stack.printAllElements()

stack.isEmpty
stack.pop()

stack.push(3)
stack.printAllElements()
```

# 链表

##### 链表的的定义
> 链表是一种物理存储单元上非连续、非顺序的存储结构，数据元素的逻辑顺序是通过链表中的指针链接次序实现的。

而且由于数据元素所持有的指针个数和链接特性可以将链表分为：

* 单向链表：单向链表的链接方向是单向的，其中每个结点都有指针成员变量指向列表中的下一个结点；
* 双向链表：双向链表的每个数据结点中都有两个指针，分别指向直接后继和直接前驱。所以，从双向链表中的任意一个结点开始，都可以很方便地访问它的前驱结点和后继结点，它的链接方向是双向的。
* 循环链表：循环链表是另一种形式的链式存贮结构。它的特点是表中最后一个结点的指针域指向头结点，整个链表形成一个环。

##### 双向链表的结构
![双向链表](https://upload-images.jianshu.io/upload_images/1102036-c89f024c6db0ad30?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

##### 双向链表的实现

```
public class LinkedListNode<T> {
    
    //value of a node
    var value: T
    
    //pointer to previous node
    weak var previous: LinkedListNode?
    
    //pointer to next node
    var next: LinkedListNode?
    
    
    //init
    public init(value: T) {
        self.value = value
    }
}



public class LinkList<T> {

    public typealias Node = LinkedListNode<T>
    
    /** first node*/
    private var head: Node?
    
    /** empty*/
    var isEmpty: Bool {
        return head == nil
    }
    
    /** count of node*/
    var count: Int {
        guard var node = head else { return 0 }
        var count = 1
        while let next = node.next {
            node = next
            count += 1
        }
        return count
    }
    /** first node*/
    var first: Node? {
        return head
    }
    /** last node*/
    var last: Node? {
        guard var node = head else { return nil }

        while let next = node.next {
            node = next
        }
        return node
    }
    
    /** get node of index*/
    public func node(atIndex index: Int) -> Node? {
        
        if isEmpty {
            return nil
        } else {
            if index >= count {
                return nil
            }
            var node = head
            for _ in 0..<index {
                node = node?.next
                if node == nil {
                    break
                }
            }
            return node
        }
    }

    public func printAllNodes(){
        
        guard head != nil else {
            print("linked list is empty")
            return
        }
        
        var node = head
        
        print("\nstart printing all nodes:")
        
        for index in 0..<count {
            
            if node == nil {
                break
            }
            
            print("[\(index)]\(node!.value)")
            node = node!.next
            
        }
    }
    
}

extension LinkList {
    /** insert node at last index*/
    public func appendToTail(value: T) {
        let newNode = Node(value: value)
        
        if let lastNode = last {
            lastNode.next = newNode
            newNode.previous = lastNode
        } else {
            head = newNode
        }
    }
    
    /** insert node to index 0*/
    public func insertToHead(value: T) {
        
        let newNode = Node(value: value)
        
        if let headNode = head {
            newNode.next = headNode
            headNode.previous = newNode
            head = newNode
        } else {
            head = newNode
        }
    }
    
    /** insert node in specific index*/
    public func insert(_ value: T, atIndex index: Int) {
        
        let newNode = Node(value: value)
        
        if index < 0 {
            fatalError("无效的index")
        }
        
        if count == 0 {
            head = newNode
        } else {
            if index == 0 {
                head = newNode
            } else {
                if index > count {
                    fatalError("index 超出 count")
                } else {
                    let prev = node(atIndex: index - 1)
                    let next = prev?.next
                    newNode.previous = prev
                    prev?.next = newNode
                    newNode.next = next
                    next?.previous = newNode
                }
            }
        }
    }
}

extension LinkList {
    
    /** remove all node*/
    public func removeAll() {
        head = nil
    }
    
    /** remove last node*/
    public func removeLast() -> T? {
        guard let last = last else { return nil }
        return remove(node: last)
    }
    
    /** remove a node by it's refrence*/
    public func remove(node: Node) -> T? {
        guard head == nil else {
            print("linked list is empty")
            return nil
        }
        
        let pre = node.previous
        let next = node.next
        
        if let prev = pre {
            prev.next = next
        } else {
            head = next
        }
        
        next?.previous = pre
        node.previous = nil
        node.next = nil
        return node.value
    }
    
    //remove a node by it's index
    public func removeAt(_ index: Int) -> T? {
        
        guard head != nil else {
            print("linked list is empty")
            return nil
        }
        
        let node = self.node(atIndex: index)
        guard node != nil else {
            return nil
        }
        return remove(node: node!)
    }
    
}



let list = LinkList<String>()
list.isEmpty
list.first
list.count

list.appendToTail(value: "Swift")
list.insert("Python", atIndex: 1)
list.printAllNodes()
```

#### 数组, 链表, 哈希表对比:
* 数组:
    * 优点:
        1. 数组的主要优点是根据下标值访问效率会很高
        2. 比较好的方式是先对数组进行排序, 再进行二分查找
    * 缺点:
        1. 需要先对数组进行排序, 生成有序数组, 才能提高查找效率
        2. 另外数组在插入和删除数据时, 需要有大量的位移操作(插入到首位或者中间位置的时候), 效率很低
* 链表
    * 优点:
        1. 链表的插入和删除操作效率都很高
    * 缺点:
        1. 查找效率很低, 需要从头开始依次访问链表中的每个数据项, 直到找到
* 哈希表
    * 优点:
        1. 哈希表的插入/查询/删除效率都是非常高
    * 缺点:
        1. 空间利用率不高, 底层使用的是数组
        2. 哈希表中的元素是无序的, 不能按照固定的顺序来遍历哈希表中的元素
        3. 不能快速的找出哈希表中的最大值或者最小值这些特殊的值 

#### 树
![树结构图](https://upload-images.jianshu.io/upload_images/1102036-b7548b9afa78655e?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

##### 树的术语
1. 节点的度(Degree): 节点的子树个数
2. 树的度: 树的所有结点中最大的度数. (树的度通常为结点的个数N-1)
3. 叶结点（Leaf）：度为0的结点. (也称为叶子结点)
4. 父结点（Parent）：有子树的结点是其子树的根结点
5. 子结点（Child）：若A结点是B结点的父结点，则称B结点是A结点的子结点；子结点也称孩子结点
6. 兄弟结点（Sibling）：具有同一父结点的各结点彼此是兄弟结点
7. 路径和路径长度：从结点n1到nk的路径为一个结点序列n1 , n2,… , nk, ni是 ni+1的父结点。路径所包含边的个数为路径的长度
8. 结点的层次（Level）：规定根结点在1层，其它任一结点的层数是其父结点的层数加1
9. 树的深度（Depth）：树中所有结点中的最大层次是这棵树的深度

##### 二叉树
> 如果树中每个节点最多只能有两个子节点, 这样的树就成为"二叉树". 


![二叉树的五种形态](https://upload-images.jianshu.io/upload_images/1102036-3422b18b70bba173?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)
###### 二叉树的特性
1. 一个二叉树第 i 层的最大结点数为：2^(i-1), i >= 1
2. 深度为k的二叉树有最大结点总数为:： 2^k - 1, k >= 1
3. 对任何非空二叉树 T，若n0表示叶结点的个数、n2是度为2的非叶结点个数，那么两者满足关系n0 = n2 + 1
![](https://upload-images.jianshu.io/upload_images/1102036-ec1fb08857229061?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

###### 特殊的二叉树
* 完美二叉树(Perfect Binary Tree) , 也称为满二叉树(Full Binary Tree）
    * 在二叉树中, 除了最下一层的叶结点外, 每层节点都有2个子结点, 就构成了满二叉树
    ![](https://upload-images.jianshu.io/upload_images/1102036-c7b0ef2b456f26af?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)
* 完全二叉树(Complete Binary Tree)
    * 除二叉树最后一层外, 其他各层的节点数都达到最大个数
    * 且最后一层从左向右的叶结点连续存在, 只缺右侧若干节点
    * 完美二叉树是特殊的完全二叉树
    
    > 下面不是完全二叉树, 因为D节点还没有右结点, 但是E节点就有了左右节点
    ![](https://upload-images.jianshu.io/upload_images/1102036-b89f4639a1e557ce?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)
    
###### 二叉树存储
> 二叉树的存储常见的方式是数组和链表

* 数组
    * 完全二叉树: 按从上至下、从左到右顺序存储
    ![](https://upload-images.jianshu.io/upload_images/1102036-47e375d88635b261?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)
    * 非完全二叉树:非完全二叉树要转成完全二叉树才可以按照上面的方案存储, 会造成很大的空间浪费
    ![](https://upload-images.jianshu.io/upload_images/1102036-5b6e9fa75d230845?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)
* 链表

    > 二叉树最常见的方式还是使用链表存储, 每个结点封装成一个Node, Node中包含存储的数据, 左结点的引用, 右结点的引用
    
    ![](https://upload-images.jianshu.io/upload_images/1102036-aa7d77c007778c1b?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

###### 什么是二叉搜索树
> 二叉搜索树（BST，Binary Search Tree），也称二叉排序树或二叉查找树
> 二叉搜索树是一颗二叉树, 可以为空；如果不为空，满足以下性质
>  
> * 非空左子树的所有键值小于其根结点的键值
> * 非空右子树的所有键值大于其根结点的键值
> * 左、右子树本身也都是二叉搜索树

![](https://upload-images.jianshu.io/upload_images/1102036-714d0fc1bc2a866e?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

###### 二叉搜索树的特点:
> 二叉搜索树的特点就是相对较小的值总是保存在左结点上, 相对较大的值总是保存在右结点上

###### 二叉搜索树的操作
* ``` insert(key) ```:向树中插入一个新的键
* ``` search(key) ```:在树中查找一个键，如果结点存在，则返回true；如果不存在，则返回false
* ``` inOrderTraverse ```: 通过中序遍历方式遍历所有结点
* ``` preOrderTraverse ```:通过先序遍历方式遍历所有结点
* ```postOrderTraverse ```:通过后序遍历方式遍历所有结点
* ``` min ```:返回树中最小的值/键
* ``` max ```:返回树中最大的值/键
* ``` remove(key) ```:从树中移除key
###### 搜索二叉树的实现
1. 首先定义一个节点类

     ```
     public class Node {
        
        //value of a node
        var key: Int
        
        //pointer to previous node
        var left: Node?
        
        //pointer to next node
        var right: Node?
        
        
        //init
        public init(key: Int) {
            self.key = key
        }
    }
 ```
 2. 定义一个搜索二叉树类, 声明一个root属性,只要有根节点就能找到所有的子节点
    
        ```
        public class BinarySerachTree{
            /** root node*/
            var root: Node?
        }
        ```
        
 3. 向树中插入数据

        ```
        /** insert a node*/
    func insert(key: Int) {
        let newNode = Node(key: key)
        if let root = root {
            insertNode(node: root, newNode: newNode)
        } else {
            root = newNode
        }
    }
    private func insertNode(node: Node, newNode: Node) {
        if node.key > newNode.key {
            if let left = node.left  {
                insertNode(node: left, newNode: newNode)
            } else {
                node.left = newNode
            }
        } else {
            if let right = node.right {
                insertNode(node: right, newNode: newNode)
            } else {
                node.right = newNode
            }
        }
    }
        ```
 4. 先序遍历
  
      ```
      /** 先序遍历
         *  1.访问根节点
         *  2.先序遍历左子树
         *  3.先序遍历右子树
         */
        func preOrderTraversal() {
            preOrderTranversalNode(node: root) { (key) in
                print(key)
            }
        }
        
        private func preOrderTranversalNode(node: Node?, handle: (_ key: Int) -> Void) {
            if let node = node  {
                handle(node.key)
                preOrderTranversalNode(node: node.left, handle: handle)
                preOrderTranversalNode(node: node.right, handle: handle)
            }
        }
      ```
 5. 中序遍历
 
     ```
     /** 中序遍历
         *  1.中序遍历其左子树
         *  2.访问根节点
         *  3.中序遍历其右子树
         */
        func inOrderTraversal() {
            inOrderTraversalNode(node: root) { (key) in
                print(key)
            }
        }
        
        private func inOrderTraversalNode(node: Node?, handle:(_ key: Int) -> Void) {
            if let node = node {
                inOrderTraversalNode(node: node.left, handle: handle)
                handle(node.key)
                inOrderTraversalNode(node: node.right, handle: handle)
            }
        }
     ```
 6. 后序遍历
 
     ```
     /** 后续遍历
         *  1. 后序遍历其左子树
         *  2. 后序遍历其右子树
         *  3. 访问根节点
         */
        func postOrderTraversal() {
            postOrderTraversalNode(node: root) { (key) in
                print(key)
            }
        }
        
        private func postOrderTraversalNode(node: Node?, handle:(_ key: Int) -> Void) {
            if let node = node {
                postOrderTraversalNode(node: node.left, handle: handle)
                postOrderTraversalNode(node: node.right, handle: handle)
                handle(node.key)
            }
            
        }
     ```
 7. 最大自和最小值
  ![](https://upload-images.jianshu.io/upload_images/1102036-f9f5d3c4afaeead6?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)
  
      ```
      var min: Int? {
            var node = root
            while node?.left != nil {
                node = node?.left
            }
            return node?.key
        }
        
        var max: Int? {
            var node = root
            while node?.right != nil {
                node = node?.right
            }
            return node?.key
        }
      ```
 8. 搜索特定的值        
     * 递归实现
     
         ```
         func searck(key: Int) -> Bool {
            return searchNode(node: root, key: key)
        }
        /** 递归实现*/
        private func searchNode(node: Node?, key: Int) -> Bool {
            guard let node = node else {
                return false
            }
            
            if node.key > key {
                return searchNode(node: node.left, key: key)
            } else if node.key < key {
                return searchNode(node: node.right, key: key)
            } else {
                return true
            }
        }
         ```
        *  循环实现
        
            ```
            /** 循环实现*/
        private func searchNode_while(key: Int) -> Bool {
            var node = root
            while node != nil {
                if node!.key > key {
                    node = node?.left
                } else if node!.key < key{
                    node = node?.right
                } else {
                    return true
                }
            }
            return false
        }
            ```
 9. 二叉树删除
    
        ```
        /** 二叉树删除
         *  1.节点为叶子节点(没有子节点)
         *  2.节点有一个子节点
         *  3.节点有俩个子节点
         */
        func remove(key: Int) -> Bool {
            guard root == nil else {
                return false
            }
            //1. 定义中间变量
            var current: Node? = root!
            var parent = root!
            var isLeftChild = true
            
            //2.开始查找子节点
            while current!.key != key {
                parent = current!
                if key < current!.key {
                    isLeftChild = true
                    current = current?.left
                } else {
                    isLeftChild = false
                    current = current?.right
                }
                
                if current == nil {//如果发现current已经指向nil, 那么说明没有找到要删除的数据
                    return false
                }
            }
            //3.删除的节点是叶子节点
            if current?.left == nil && current?.right == nil {
                if current?.key == root?.key {
                    root = nil
                } else if isLeftChild {
                    parent.left = nil
                } else {
                    parent.right = nil
                }
            } else if (current?.right == nil) {//4.删除有一个左子节点的节点
                if current?.key == root?.key {
                    root = current?.left
                } else if isLeftChild {
                    parent.left = current?.left
                } else {
                    parent.right = current?.left
                }
            } else if (current?.left == nil) {//4.删除有一个右子节点的节点
                if current?.key == root?.key {
                    root = current?.right
                } else if isLeftChild {
                    parent.left = current?.right
                } else {
                    parent.right = current?.right
                }
            } else {//两种实现方式, 找前驱和后继
                let successor = getSuccessor(node: current!)
                if current?.key == root?.key {
                    root = successor
                } else if isLeftChild {
                    parent.left = successor
                } else {
                    parent.right = successor
                }
                successor.left = current?.left
            }
            
            return true
        }
        //找后继
        private func getSuccessor(node: Node) -> Node {
            var successorParent:Node = node
            var successor: Node = node
            var current = node.right
            
            while current != nil {
                successorParent = successor
                successor = current!
                current = current?.left
            }
            
            if successor.key != node.right?.key {
                successorParent.left = successor.right
                successor.right = node.right
            }
            return successor
        }
        //找前驱
        private func getPrecursor(node: Node) -> Node {
            var precursorParent: Node = node
            var precursor: Node = node
            var current = node.left
            while current != nil {
                precursorParent = precursor
                precursor = current!
                current = current?.right
            }
            if precursor.key != node.left?.key {
                precursorParent.right = precursor.left
                precursor.left = node.left
            }
            return precursor
        }
        ```
        
###### 
# 排序
#### 冒泡排序
```
var array = [3, 6, 4, 2, 11, 10, 5]
/** 冒泡排序*/
func bubbleSort(array: [Int]) -> [Int] {
    var result = array
    for i in (0..<result.count).reversed() {
        for j in 0..<i {
            if result[j] > result[j+1] {
                (result[j], result[j+1]) = (result[j+1], result[j])
            }
        }
    }
    return result
}

bubbleSort(array: array)
```
#### 选择排序
```
/** 选择排序*/
func selectionSort(array: [Int]) -> [Int] {
    var result = array
    for i in 0..<result.count - 1 {
        var min = i + 1
        for j in min..<result.count {
            if result[min] > result[j] {
                min = j
            }
        }
        (result[min], result[i]) = (result[i], result[min])
    }
    return result
}

selectionSort(array: array)
```
#### 插入排序
```
/** 插入排序*/
func insertionSort(array: [Int]) -> [Int] {
    var result = array
    for i in 1..<result.count {
        var j = i
        let temp = result[j]
        while j > 0 && result[j-1] > temp {
            result[j] = result[j - 1]
            j -= 1
        }
        result[j] = temp
    }
    return result
}

insertionSort(array: array)

```
#### 希尔排序
```
/** 希尔排序呢*/
func shellSort(array: [Int]) -> [Int] {
    var result = array
    let length = array.count
    var gap = lrintf(Float(length) / 2)
    while gap > 0 {
        for i in gap..<length {
            var j = i
            let temp = result[i]
            while j > gap - 1 && result[j - gap] > temp {
                result[j] = result[j - gap]
                j -= gap
            }
            result[j] = temp
        }
        gap = lrintf(Float(gap) / 2)
    }
    return result
}
shellSort(array: array)
```




 












