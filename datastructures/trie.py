class TrieNode:

    def __init__(self, numChildren):
        self.children = [None]*numChildren
        self.isEndOfWord = False
        self.activeChildCount = 0

class Trie:

    def __init__(self, maxChildren):
        self.maxChildren = maxChildren
        self.root = TrieNode(maxChildren)        

    def getRoot(self):
        return self.root

    def insert(self, word):
        cn = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not cn.children[idx]:
                cn.children[idx] = TrieNode(self.maxChildren)
                cn.activeChildCount += 1
            cn = cn.children[idx]
        if not cn.isEndOfWord:
            cn.isEndOfWord = True
        else:
            print("word %s already exists" %word)

    def search(self, word):
        cn = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not cn.children[idx]:
                return False
            cn = cn.children[idx]
        return cn.isEndOfWord

    def delete(self, word):
        cn = self.root
        path = []
        for c in word:
            idx = ord(c) - ord('a')
            # If the letter is not there, return
            if not cn.children[idx]:
                return False
            path.append((cn, idx))
            cn = cn.children[idx]
        # If the end of word mark is not set, return
        if not cn.isEndOfWord:
            return False
        i, pathLen = 0, len(path)
        while i < pathLen:
            tup = path.pop()
            cn.isEndOfWord = False
            if cn.activeChildCount == 0:
                tup[0].children[tup[1]] = None
                tup[0].activeChildCount -= 1
            cn = tup[0]
            i += 1
        
        return True

    def dfsTrie(self, node):
        idx = 0
        for child in node.children:
            if not child:
                idx += 1
                continue
            val = chr(idx + ord('a'))
            print("Node:{} activeChildCount:{} isEndOfWord:{}".format(val, child.activeChildCount, child.isEndOfWord))
            self.dfsTrie(child)
            idx += 1

# Test
T = Trie(26)
words = ["man", "mani", "manila", "mankind"]
for w in words:
    print("Word to insert: %s" %w)
    T.insert(w)

T.dfsTrie(T.getRoot())

words = ["man", "mano", "ma", "mass"]
for w in words:
    print("Word {} exists in trie: {}".format(w, T.search(w)))

words = ["man", "mani", "manila", "man", "mankind"]
for w in words:
    print("Word {} is deleted from trie: {}".format(w, T.delete(w)))
    T.dfsTrie(T.getRoot())

