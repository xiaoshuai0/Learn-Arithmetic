class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def preOrder(self, root):
        if root == None: return []
        print(root.val)
        lefts = self.preOrder(root.left)
        rights = self.preOrder(root.right)
        return [root.val] + lefts + rights

    def inOrder(self, root):
        if root == None: return []
        lefts = self.inOrder(root.left)
        print(root.val)
        rights = self.inOrder(root.right)
        return lefts + [root.val] + rights

    def inOrderStack(self, root):
        res = []
        stack = []
        curr = root
        while curr != None or len(stack) != 0:
            while curr != None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res

    def postOrder(self, root):
        if root == None: return []
        lefts = self.postOrder(root.left)
        rights = self.postOrder(root.right)
        print(root.val)
        return lefts + rights + [root.val]

    def layerOrder(self, root):
        if root == None: return
        list = []
        current, next = 0, 0
        list.append(root)
        current = 1
        next = 0
        while len(list) != 0:
            currentNode = list.pop(0)
            print(currentNode.val)
            current -= 1
            if currentNode.left != None:
                list.append(currentNode.left)
                next += 1
            if currentNode.right != None:
                list.append(currentNode.right)
                next += 1
            if current == 0:
                current = next
                next = 0

    def layerOrder2(self, root):
        if root == None: return
        list, result = [], []
        list.append(root)
        while len(list) !=0:
            size  = len(list)
            li = []
            for i in range(size):
                current = list.pop(0)
                li.append(current.val)
                if current.left != None:
                    list.append(current.left)
                if current.right != None:
                    list.append(current.right)
            result.append(li)
        return result

    def findInBinarySearchTree(self, root, data):
        while root != None:
            if data < root.val: root = root.left
            elif data > root.val: root = root.right
            else: return  root.val
        return None

    # def insertInBinarySearchTree(self, root, data):





if __name__ == "__main__":
    root = Tree('A')
    node1 = Tree('B')
    node2 = Tree('C')
    node3 = Tree('D')
    node4 = Tree('E')
    node5 = Tree('F')
    node6 = Tree('G')
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = node5
    node2.right = node6
    # Solution().preOrder(root)
    print(Solution().inOrder(root))
    print(Solution().inOrderStack(root))
    # Solution().postOrder(root)
    # Solution().layerOrder(root)
    # print(Solution().layerOrder2(root))