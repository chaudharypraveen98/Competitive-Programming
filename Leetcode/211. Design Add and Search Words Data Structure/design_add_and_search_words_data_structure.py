class WordNode():
    def __init__(self):
        self.children = {}
        self.isWordEnd = False


class WordDictionary(object):

    def __init__(self):
        self.root = WordNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = WordNode()
            curr = curr.children[ch]
        curr.isWordEnd = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(idx, node):
            if idx == len(word):
                return node.isWordEnd
            ch = word[idx];
            if ch == ".":
                for childNode in node.children.values():
                    if dfs(idx+1, childNode):
                        return True
                return False
                
            elif ch not in node.children:
                return False
            return dfs(idx+1,node.children[ch])
        return dfs(0,self.root)


operations = ["addWord", "addWord", "addWord", "addWord", "search", "search",
              "addWord", "search", "search", "search", "search", "search", "search"]
values = [["at"], ["and"], ["an"], ["add"], ["a"], [".at"], [
    "bat"], [".at"], ["an."], ["a.d."], ["b."], ["a.d"], ["."]]

wordDictionary = WordDictionary()
for i in range(len(operations)):
    if (operations[i] == "addWord"):
        wordDictionary.addWord(values[i][0])
    else:
        print(wordDictionary.search(values[i][0]))
