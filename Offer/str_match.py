class Solution:
    def brute_force(self, a, b):
        m, n = len(a), len(b)
        if m < n:
            return False
        for i in range(m - n + 1):
            res = False
            for j in range(n):
                if b[j] != a[i + j]:
                    res = False
                    break
                else:
                    res = True
            if res: return True
        return False

    def brute_force2(self, a, b):
        m, n = len(a), len(b)
        if m < n:
            return False
        for i in range(m - n + 1):
            print(a[i: i + n])
            if a[i: i + n] == b:
                return True
        return False

    def Rabin_karp(self, a, b):
        powList = []
        bhash = 0
        m, n = len(a), len(b)
        for i in range(n):
            powList.append(pow(26, i))

        for i in range(n):
            bhash += (ord(b[i]) - ord('a')) * powList[n - 1 - i]

        aHash = 0
        for i in range(len(a)):
            if i < n - 1:
                aHash += (ord(a[i]) - ord('a')) * powList[n - 2 - i]
            else:
                aHash = 26 * aHash + (ord(a[i]) - ord('a'))
                if aHash == bhash:
                    return True
                fistHash = (ord(a[i - (n - 1)]) - ord('a')) * powList[n - 1]
                aHash -= fistHash
        return False

    def byor_moore(self, a, b):
        m, n = len(a), len(b)
        if m < n:
            return False
        index = 0
        while index <= m - n:
            if a[index - n : index] == b:
                return True









if __name__ == "__main__":
    print(Solution().brute_force('abcdefg', 'efe'))
    print(Solution().Rabin_karp('abcdefg', 'efg'))