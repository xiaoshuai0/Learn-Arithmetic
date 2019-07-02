class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # dict1, dict2 = {}, {}
        # for item in s:
        #     dict1[item] = dict1.get(item, 0) + 1
        # for item in t:
        #     dict2[item] = dict2.get(item, 0) + 1
        # return dict1 == dict2
        dict1, dict2 = [0] * 26, [0] * 26
        for item in s:
            dict1[ord(item) - ord('a')] += 1
        for item in t:
            dict2[ord(item) - ord('a')] += 1
        return dict1 == dict2


if __name__ == "__main__":
    print(Solution().isAnagram('anagra', 'nagaram'))