# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        inOrderList = self.inOrder(root)
        return inOrderList == list(sorted(set(inOrderList)))

    def inOrder(self, root):
        if root is None:
            return []
        return self.inOrder(root.left) + [root.val] + self.inOrder(root.right)

    def isValidBST2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.prev = None
        return self._helper(root)

    def _helper(self, root):
        if root is None: return True
        if not self._helper(root.left):
            return False
        if self.prev and self.prev.val >= root.val:
            return False
        self.prev = root
        return self._helper(root.right)

    def isValidBST3(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def _helper(root, min = None, max = None):
            if root is None: return True
            if min != None and root.val <= min: return False
            if max != None and root.val >= max: return False
            return _helper(root.left, min, root.val) and _helper(root.right, root.val, max)
        return _helper(root)

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """


if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(Solution().isValidBST1(root))
    print(Solution().isValidBST2(root))
    print(Solution().isValidBST3(root))