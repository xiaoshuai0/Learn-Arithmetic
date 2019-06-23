# 找出数组重复的数字
# 在长度为n的数组里的所有数字都是0~n-1的范围. 数组中某些数字是重复的, 但不知道有几个数字重复, 也不知道每个数字重复几次.
# 请找出数组中任意一个重复的数组.
# 例如, 如果输入长度为7的数组{2, 3, 1, 0, 2, 5, 3}, 那么对应的输出是重复的数字2或者3.

def duplicate(nums):
    count = len(nums)
    if count < 2:
        return None
    # 长度为n的数组里的所有数字都是0~n-1的范围
    for i in range(count):
        if nums[i] < 0 or nums[i] > count - 1:
            return None
    result = None
    for i in range(count):
        while nums[i] != i:
            if nums[i] == nums[nums[i]]:
                result = nums[i]
                return result
            temp = nums[i]
            nums[i] = nums[temp]
            nums[temp] = temp
    return None


if __name__ == "__main__":
    result = duplicate([2, 3, 1, 0, 2, 5, 3])
    print(result)
