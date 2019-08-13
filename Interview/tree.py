class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None or root == p or root == q: return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is None:
            return right
        if right is None:
            return left
        return root
    # 二叉搜索树
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

    def isValidBST(self, root):
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

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.prev = None
        def _helper(root):
            if root is None: return True
            if not _helper(root.left, self.prev):
                return False
            if self.prev and self.prev.val > root.val:
                return False
            self.prev = root
            return _helper(root.right)
        return _helper(root)


    def pow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n > 0:
            if n & 1:
                pow *= x
            x *= x
            x >>= 1
        return pow

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for item in nums:
            if item not in dict:
                dict[item] = 0
            dict[item] = dict[item] + 1
            if dict[item] > (len(nums) // 2): return item
        ans, count = nums[0], 0
        for (key, value) in dict:
            if value > count:
                ans, count = key, value
        return ans

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(0, len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > ans:
                    ans = profit
        return ans

    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice, maxProfit = 0, 0

        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice
        return maxProfit

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # if root is None: return 0
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        stack = []
        if root is not None:
            stack.append((1, root))
        depth = 0
        while len(stack) != 0:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))
        return depth

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # if root is None: return 0
        # if root.left is None: return self.minDepth(root.right) + 1
        # if root.right is None: return self.minDepth(root.left) + 1
        # return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

        stack = []
        if root is not None:
            stack.append((1, root))
        else:
            return 0
        import sys
        depth = sys.maxsize
        while len(stack) > 0:
            current_depth, root = stack.pop(0)
            if root.left is None and root.right is None:
                depth = min(depth, current_depth)

            if root.left is not None:
                stack.append((current_depth + 1, root.left))

            if root.right is not None:
                stack.append((current_depth + 1, root.right))

        return depth





if __name__ == "__main__":

    print(Solution().maxProfit([7,1,5,3,6,4]))


