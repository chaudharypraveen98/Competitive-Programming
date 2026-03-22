class TrieNode():
    def __init__(self):
        self.childrens = {}
        self.isWordEnd = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for ch in word:
            if not ch in curr.childrens:
                curr.childrens[ch] = TrieNode()
            curr = curr.childrens[ch]
        curr.isWordEnd = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for ch in word:
            if ch not in curr.childrens:
                return False
            curr = curr.childrens[ch]
        return curr.isWordEnd
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for ch in prefix:
            if ch not in curr.childrens:
                return False
            curr = curr.childrens[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)