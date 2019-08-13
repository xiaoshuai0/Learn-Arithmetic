# class TrieNode:
#     def __init__(self, data):
#         self.data = data
#         self.children = [''] * 26
#         self.isEndingChar = False
#
# class Trie:
#     root = TrieNode('/') # 存储无意义字符
#
#     def insert(self, text):
#         p = self.root
#         for ch in text:
#             index = ord(ch) - ord('a')
#             if p.children[index] == '':
#                 newNode = TrieNode(ch)
#                 p.children[index] = newNode
#             p = p.children[index]
#         p.isEndingChar = True
#
#     def find(self, pattern):
#         p = self.root
#         for ch in pattern:
#             index  = ord(ch) - ord('a')
#             if p.children[index] == '': return False
#             p = p.children[index]
#         if p.isEndingChar == False: return False
#         else: return True
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end = -1

    def insert(self, word):
        """
        Inserts a word into the trie.
        :param word: str
        :return:
        """
        curNode = self.root
        for ch in word:
            if not ch in curNode:
                curNode[ch] = {}
            curNode = curNode[ch]
        curNode[self.end] = True

    def search(self, word):
        """
        Return if the word is in the trie
        :param word:
        :return:
        """
        curNode = self.root
        for ch in word:
            if not ch in curNode:
                return False
            curNode = curNode[ch]
        return True if self.end in curNode else False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :param prefix:
        :return:
        """
        curNode = self.root
        for ch in prefix:
            if not ch in curNode:
                return False
            curNode = curNode[ch]
        return True

    def get_start(self, prefix):
        """

        :param prefix:
        :return:
        """
        def get_key(pre, pre_node):
            res = []
            if pre_node.get(self.end):
                res.append(pre)
            for key in pre_node.keys():
                if key != self.end:
                    res.extend(get_key(pre + key, pre_node.get(key)))
            return res

        if not self.startsWith(prefix):
            return []
        else:
            curNode = self.root
            for p in prefix:
                curNode = curNode.get(p)
            else:
                return get_key(prefix, curNode)





if __name__ == "__main__":
    # trie = Trie()
    # trie.insert('how')
    # trie.insert('hi')
    # trie.insert('her')
    # trie.insert('hello')
    # trie.insert('so')
    # trie.insert('see')
    #
    # print(trie.find('how'))

    trie = Trie()
    trie.insert("Python")
    trie.insert("Python 算法")
    trie.insert("Python web")
    trie.insert("Python web 开发")
    trie.insert("Python web 开发 视频教程")
    trie.insert("Python 算法 源码")
    trie.insert("Perl 算法 源码")
    print(trie.search("Perl"))
    print(trie.search("Perl 算法 源码"))
    print((trie.get_start('P')))
    print((trie.get_start('Python web')))
    print((trie.get_start('Python 算')))
    print((trie.get_start('P')))
    print((trie.get_start('Python web')))
    print((trie.get_start('Python 算')))
