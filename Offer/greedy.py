class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        count = [0] * 1001
        for trip in trips:
            count[trip[1]] += trip[0]
            count[trip[2]] -= trip[0]

        if count[0] > capacity: return False
        for i in range(1, 1001):
            count[i] += count[i - 1]
            if count[i] > capacity:
                return False
        return True






if __name__ == "__main__":
    print(Solution().carPooling([[2,1,5],[3,3,7]], 4))
    print(Solution().carPooling([[2,1,5],[3,3,7]], 5))
    print(Solution().carPooling([[2,1,5],[3,5,7]], 3))
    print(Solution().carPooling([[3,2,7],[3,7,9],[8,3,9]], 11))
