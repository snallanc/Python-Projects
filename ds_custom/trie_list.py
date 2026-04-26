"""
Trie Implementation where each trie node maintains its children in a fixed sized list(26):
"""

# Trie node class
class TrieNode:

    def __init__(self, numChildren):
        self.children = [None]*numChildren
        self.isEndOfWord = False
        self.numUsers = 0

# Trie class
class Trie:

    def __init__(self, maxChildren):
        self.maxChildren = maxChildren
        self.root = TrieNode(maxChildren)

    def getRoot(self):
        return self.root

    def insert(self, word):
        # First check if the word already exists in the trie
        if self.search(word):
            print("\tword \"{0}\" already exists".format(word))
            return

        # If not, insert the word
        cn = self.root
        for c in word:
            # Use the ASCII value diff as the index
            idx = ord(c) - ord('a')
            if not cn.children[idx]:
                cn.children[idx] = TrieNode(self.maxChildren)
                cn.numUsers += 1
            cn = cn.children[idx]
        cn.isEndOfWord = True

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
            # Append the parent node and the idx as a tuple
            path.append((cn, idx)) # (parent-node, current-idx)
            cn = cn.children[idx]
        # If the end of word mark is not set, return
        if not cn.isEndOfWord:
            return False

        # We found the word, mark that this word is no longer searchable in the trie
        cn.isEndOfWord = False
        if cn.numUsers:
            # This end of word node has children, skip further processing
            return True

        # We have the word and its path, now backtrack the path and delete the word
        i, pathLen, = 0, len(path)
        while i < pathLen:
            parent, childIdx = path.pop() # (parent-node, current-idx)

            # If current node(cn) has no users and is not the end of word, decrement the numUsers of the parent and unlink cn from its parent
            # Else, no further processing is required
            if not cn.numUsers and not cn.isEndOfWord:
                parent.children[childIdx] = None
                parent.numUsers -= 1
            else:
                break

            # Repeat the above steps for the parent node
            cn = parent

            i += 1

        return True

    def dfsTrie(self, node):
        idx = 0
        for child in node.children:
            if not child:
                idx += 1
                continue
            val = chr(idx + ord('a'))
            print("\tNode:{0} numUsers:{1} isEndOfWord:{2}".\
                  format(val, child.numUsers, child.isEndOfWord))
            self.dfsTrie(child)
            idx += 1

'''
Test Code
'''

def divider():
    print("\n===========================================\n")

T = Trie(26)
words = ["man", "mani", "manila", "mankind", "man"]
print("Insert words:")
for w in words:
    print("\tWord to insert: \"{0}\"".format(w))
    T.insert(w)
divider()

print("DFS traversal of all nodes:")
T.dfsTrie(T.getRoot())
divider()

print("Search nodes:")
words = ["man", "mano", "ma", "manil", "manila", "mankind"]
for w in words:
    print("\tWord \"{0}\" exists in trie: {1}".format(w, T.search(w)))
divider()

words = ["mankind", "mani", "manila", "mankind", "man"]
print("Delete nodes:")
for w in words:
    print("\tWord \"{0}\" is deleted from trie: {1}".format(w, T.delete(w)))
    T.dfsTrie(T.getRoot())
    divider()

