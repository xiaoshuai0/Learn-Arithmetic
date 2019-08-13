class MyHeap:

    def __init__(self, capacity):
        self.a = [0] * (capacity + 1)   # 数组, 从下标1开始存储数据
        self.n = capacity               # 堆可以存储的最大数据个数
        self.count = 0                  # 堆中已经存储的数据个数

    # 堆中插入元素
    def insert(self, data):
        if self.count >= self.n: return #堆满了
        self.count += 1
        self.a[self.count] = data
        i = self.count
        while i // 2 > 0 and self.a[i] > self.a[i // 2]:
            self.swap(i, i // 2)
            i = i // 2

    def removeMax(self):
        if self.count == 0: return
        self.a[1] = self.a[self.count]
        self.a[self.count] = 0
        self.count -= 1
        self.a = self.heapify(self.a , self.count, 1)

    def heapify(self, nums, n, i):
        while True:
            maxPos = i
            if i * 2 < n and nums[i] < nums[i * 2]: maxPos = i * 2
            if i * 2 + 1 < n and nums[maxPos] < nums[i * 2 + 1]: maxPos = i * 2 + 1
            if maxPos == i: break
            nums[i], nums[maxPos] = nums[maxPos], nums[i]
            i = maxPos
        return nums


    def swap(self, indexOne, indexTwo):
        self.a[indexOne], self.a[indexTwo] = self.a[indexTwo], self.a[indexOne]


    def sort(self, nums):
        nums = self.buildHeap(nums)
        k = len(nums) - 1
        while k > 1:
            nums[1], nums[k] = nums[k], nums[1]
            k -= 1
            self.heapify(nums, k, 1)
        print(nums)

    def buildHeap(self, nums):
        list = [0] + nums
        count = len(nums)
        for i in reversed(range(1, count // 2 + 1)):
            self.heapify(list, count, i)
        return list

if __name__ == "__main__":
    heap = MyHeap(15)
    heap.insert(17)
    heap.insert(33)
    heap.insert(21)
    heap.insert(16)
    heap.insert(13)
    heap.insert(15)
    heap.insert(9)
    heap.insert(5)
    heap.insert(6)
    heap.insert(7)
    heap.insert(8)
    heap.insert(1)
    heap.insert(2)
    heap.insert(22)
    # heap.removeMax()
    print(heap.a)
    # heap.removeMax()
    # print(heap.a)
    # heap.removeMax()
    # print(heap.a)
    # heap.removeMax()
    # print(heap.a)
    # heap.removeMax()
    # print(heap.a)

    heap.sort([7, 5, 19, 8, 4, 1, 20, 13, 16])