'''
Binary Search Tree Implementation
'''

# Binary Search Tree Node
class BstNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Binary Search Tree
class Bst:
    def __init__(self, rootKey):
        self.root = BstNode(rootKey)

    def _sanity_check_failed(self):
        if not self.root:
            print("Tree is not initialized yet!")
            return True
        return False

    def _get_successor_node(self, node):
        '''
        Successor will be the right most node of the left subtree of the given node
        '''
        if not node or not node.left:
            return None
        pn = node
        sn = node.left
        while sn.right:
            pn, sn = sn, sn.right
        if pn != node:
            pn.right = None
        return sn

    def _searchKey(self, key):
        if self._sanity_check_failed():
            return
        pn, cn = None, self.root
        while cn:
            if key == cn.key:
                print("Node {} with search key {} found!".format(cn, key))
                return cn, pn
            elif key < cn.key:
                pn = cn
                cn = cn.left
            else:
                pn = cn
                cn = cn.right
        print("Node {} with search key {} is not found!".format(cn, key))
        return None, None

    def getRoot(self):
        return self.root

    def getSmallest(self):
        if self._sanity_check_failed():
            return
        cn = self.root
        while cn.left:
            cn = cn.left
        print("Node {} with the smallest key {}".format(cn, cn.key))
        return cn

    def getLargest(self):
        if self._sanity_check_failed():
            return
        cn = self.root
        while cn.right:
            cn = cn.right
        print("Node {} with the largest key {}".format(cn, cn.key))
        return cn

    def insert(self, key):
        if self._sanity_check_failed():
            return
        print("Insert a node with key {}".format(key))
        cn = self.root        
        nn = BstNode(key)
        while cn and cn.left and cn.right:
            if key <= cn.key:
                cn = cn.left
            else:
                cn = cn.right
        if key <= cn.key:
                tmpn = cn.left
                cn.left = nn
                nn.left = tmpn
        else:
                tmpn = cn.right
                cn.right = nn
                nn.right = tmpn

    def search(self, key):
        return self._searchKey(key)[0]
        
    def delete(self, key):
        if self._sanity_check_failed():
            return
        
        pn, cn = None, self.root
        delRoot = True if cn.key == key else False
        print("Delete a node with key {} root node? {}".format(key, delRoot))
        '''
        Possibilities:
        1. root node or any node with left and right subtrees is deleted
           - Find the successor to occupy the place of deleted node
           - Detach the successor from its parent
           - Set the left, right pointers of the successor
           - If the root is deleted, set the successor as the new root
        2. leaf node gets deleted
           - left/right of the parent can be set to None
        '''
        
        if not delRoot:
            cn, pn = self._searchKey(key)
                
        if not cn:
            print("Node with key {} doesn't exist".format(key))
            return
        print("Node {} with key {} to be deleted is found".format(cn, key))

        # Find the successor
        sn = self._get_successor_node(cn)
        
        # Update the pointer of the parent node to point to the successor node
        if pn:
            if pn.left == cn:
                pn.left = sn
            else:
                pn.right = sn

        # Set the pointers of the successor node
        if sn:
            print("Successor node {} with key {}".format(sn, sn.key))
            sn.left = cn.left if sn != cn.left else None
            sn.right = cn.right

        # Update root
        if delRoot:
            sn.left, sn.right = self.root.left, self.root.right
            self.root = sn

    # Inorder traversal prints the keys in sorted order
    def inOrderTraversal(self, node):
        if not node:
            return
        if node.left:
            self.inOrderTraversal(node.left)
        print("{}".format(node.key))
        if node.right:
            self.inOrderTraversal(node.right)

    def preOrderTraversal(self, node):
        if not node:
            return
        print("{}".format(node.key))
        if node.left:
            self.preOrderTraversal(node.left)
        if node.right:
            self.preOrderTraversal(node.right)

    def postOrderTraversal(self, node):
        if not node:
            return
        if node.left:
            self.postOrderTraversal(node.left)
        if node.right:
            self.postOrderTraversal(node.right)
        print("{}".format(node.key))


'''
Test code
'''
def _testInsert(bst):
    nodes = [50, 150, 25, 75, 125, 175, 15, 35, 65, 85, 115, 135, 165, 185]
    for n in nodes:
        bst.insert(n)
    bst.getSmallest()
    bst.getLargest()
    bst.inOrderTraversal(bst.getRoot())
    print("")

def _testSearch(bst):
    snodes = [150, 45, 65, 95, 175]
    for n in snodes:
        bst.search(n)

def _testDelete(bst):
    dnodes = [50, 15, 100, 125, 185]
    for n in dnodes:
        bst.delete(n)
        bst.getSmallest()
        bst.getLargest()
        bst.inOrderTraversal(bst.getRoot())
        print("")

bst = Bst(100)
_testInsert(bst)
_testSearch(bst)
_testDelete(bst)
