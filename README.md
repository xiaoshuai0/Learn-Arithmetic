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









