class ListNode(object):
    def __init__(self, x, key):
        self.val = x
        self.key = key
        self.next = None
        self.pre = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = None
        if key in self.cache:
            print(self.cache.get(key))
            node = self.cache.get(key)
        if node: #存在node需要将该节点放到
            self.bringNodeToHead(node)
            return node.val
        else:
            return None


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        node = self.get(key)
        if node:
            node.val = value
            self.bringNodeToHead(node)
        else:
            node = ListNode(value, key=key)
            self.insertNodeToHead(node)
        self.trim()


    def removeNode(self, node):
        del self.cache[node.key]

        if node.next: node.next.pre = node.pre
        if node.pre: node.pre.next = node.next
        if node == self.head: self.head = node.next
        if node == self.tail: self.tail = node.pre

    def trim(self):
        while len(self.cache) > self.capacity:
            self.removeNode(self.tail)




    def insertNodeToHead(self, node):
        self.cache[node.key] = node
        if self.head:
            node.next = self.head
            self.head.pre = node
            self.head = node
        else:
            self.head = self.tail = node



    def bringNodeToHead(self, node):
        if self.head == node: return

        if self.tail == node:
            self.tail = node.pre
            self.tail = None
        else:
            node.next.pre = node.pre
            node.pre.next = node.next
        node.next = self.head
        node.pre = None
        self.head.pre = node
        self.head = node

if __name__ == "__main__":
    obj = LRUCache(4)
    param_1 = obj.get('a')
    obj.put('a','10')
    obj.put('b', '10')
    obj.put('c', '10')
    obj.put('d', '10')
    obj.put('e', '10')
    obj.put('f', '10')

    print(obj.get('a'))