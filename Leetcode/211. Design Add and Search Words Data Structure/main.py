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
        curr  = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = WordNode()
            curr = curr.children[ch]
        curr.isWordEnd = True
        

    def search(self, word, idx=0,curRoot = None):
        """
        :type word: str
        :rtype: bool
        """
        curr = curRoot or self.root
        for chIdx in range(idx, len(word)):
            if word[chIdx]==".":
                return any(self.search(word, chIdx+1,curr.children[child]) for child in curr.children.keys())
            elif word[chIdx] not in curr.children:
                return False
            curr = curr.children[word[chIdx]]
        return curr.isWordEnd

operations = ["addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]
values = [["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]

wordDictionary = WordDictionary()
for i in range(len(operations)):
    if(operations[i]=="addWord"):
        wordDictionary.addWord(values[i][0])
    else:
        print(wordDictionary.search(values[i][0]))