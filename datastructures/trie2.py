"""
Trie Implementation where each trie node maintains its children in a dictionary:
"""

# Trie node class
class TrieNode:

    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

# Trie class
class Trie:

    def __init__(self, maxChildren):
        self.maxChildren = maxChildren
        self.root = TrieNode()

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
            if c not in cn.children:
                cn.children[c] = TrieNode()
            cn = cn.children[c]
        cn.isEndOfWord = True

    def search(self, word):
        cn = self.root
        for c in word:
            if c not in cn.children:
                return False
            cn = cn.children[c]
        return cn.isEndOfWord

    def delete(self, word):
        cn = self.root
        path = []

        for c in word:
            # If the letter is not there, return
            if c not in cn.children:
                return False
            # Append the parent node and the letter to be used later
            path.append((cn, c)) #(parent_node, letter)
            cn = cn.children[c]
        # If the end of word mark is not set, just return
        if not cn.isEndOfWord:
            return False

        # We found the word, mark that this word is no longer searchable in the trie
        cn.isEndOfWord = False
        if cn.children.__len__():
            # This end of word node has children, so it should not be unlinked from its ancestors
            return True

        # We have the word and its path, now backtrack the path and delete the word
        i, pathLen, = 0, len(path)
        while i < pathLen:
            parent, c = path.pop()

            # cn: current node, parent: its parent

            # If cn has no children and is not the end of word, unlink the node from its parent. Else bail out.
            # Else, no further processing is required
            if not cn.children.__len__() and not cn.isEndOfWord:
                del parent.children[c]
            else:
                break

            # Repeat the above steps for the parent node
            cn = parent

            i += 1

        return True

    def dfsTrie(self, node):
        for char, child in node.children.items():
            print("\tNode:{0} numChildren:{1} isEndOfWord:{2}".format(char, child.children.__len__(), child.isEndOfWord))
            self.dfsTrie(child)

'''
Test Code
'''

def divider():
    print("\n===========================================\n")

T = Trie(26)
words = ["man", "mannerism", "manila", "mankind", "man", "manhattan"]
print("Insert words:")
for w in words:
    print("\tWord to insert: \"{0}\"".format(w))
    T.insert(w)
divider()

print("DFS traversal of all nodes:")
T.dfsTrie(T.getRoot())
divider()

print("Search nodes:")
words = ["man", "manner", "manil", "manila", "mankind", "man-hattan"]
for w in words:
    print("\tWord \"{0}\" exists in trie: {1}".format(w, T.search(w)))
divider()

print("Delete nodes:")
words = ["mankind", "mani", "manila", "mankind", "man", "manhattan", "mannerism"]
for w in words:
    res = T.delete(w)
    print("\tWord \"{0}\" is deleted from trie: {1}".format(w, res))
    if res: # print trie only if delete went through
        T.dfsTrie(T.getRoot())
    divider()

