class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
                  left_part          |        right_part
    A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
    B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]
        """
        # list = nums1 + nums2
        # list.sort()
        # if len(list) % 2 == 0:
        #     middle = len(list) // 2
        #     return (list[middle] + list[middle - 1]) / 2.0
        # else:
        #     middle = len(list) // 2
        #     return list[middle]
        m, n = len(nums1), len(nums2)
        if m > n:
            m, n, nums1, nums2 = n, m, nums2, nums1
        iMin, iMax, hanlLen = 0, m, (m + n + 1) // 2
        while iMin <= iMax:
            i = (iMin + iMax) // 2
            j = hanlLen - i
            if i < iMax and nums2[j - 1] > nums1[i]:
                iMin = i + 1
            elif i > iMin and nums1[i - 1] > nums2[j]:
                iMax = i - 1
            else:
                maxLeft = 0
                if i == 0: maxLeft = nums2[j - 1]
                elif j == 0: maxLeft = nums1[i - 1]
                else: maxLeft = max(nums1[i - 1], nums2[j - 1])
                if (m + n) % 2 == 1: return maxLeft

                minRight = 0
                if i == m: minRight = nums2[j]
                elif j == n: minRight = nums1[i]
                else:minRight = min(nums1[i], nums2[j])

                return (maxLeft + minRight) / 2.0
        return 0.0



if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([1, 2], [3, 4, 5]))