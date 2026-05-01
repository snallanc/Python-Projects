'''
Binary Search Tree Implementation
Operations: search/insert/delete O(h) | h=log n balanced, h=n worst case | space O(n)
'''
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'traversals'))
from tree_traversals import inorder_traversal, preorder_traversal, postorder_traversal

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
            print("\t\tTree is not initialized yet!")
            return True
        return False

    def _getSuccessorNode(self, node):
        """ Successor will be the right most node of the left subtree of the given node. It is always a leaf node """
        if not node or not node.left:
            return None
        pn, sn = node, node.left
        while sn.right:
            pn, sn = sn, sn.right
        if pn != node:
            pn.right = None
        return sn

    def _searchKey(self, key):
        """ Searches for the given key; if found returns True and sets the node and parent objects. """

        pn, cn = None, self.root
        while cn:
            if key == cn.key:
                print("\t\tNode {} with search key {} found!".format(cn, key))
                return True, cn, pn
            elif key < cn.key:
                pn = cn
                cn = cn.left
            else:
                pn = cn
                cn = cn.right
        print("\t\tNode with search key {} is not found!".format(key))
        return False, None, None

    def getRoot(self):
        return self.root

    def getSmallest(self):
        """ Leftmost node is the node with the smallest key. """
        if self._sanity_check_failed():
            return None

        cn = self.root
        while cn.left:
            cn = cn.left
        print("\t\tNode {} with the smallest key {}".format(cn, cn.key))
        return cn

    def getLargest(self):
        """ Rightmost node is the node with the largest key. """
        if self._sanity_check_failed():
            return None
        cn = self.root
        while cn.right:
            cn = cn.right
        print("\t\tNode {} with the largest key {}".format(cn, cn.key))
        return cn

    def insert(self, key):
        if self._sanity_check_failed():
            return

        # If the node already exists, just return
        ret, cn, pn = self._searchKey(key)
        if ret:
            print("\tNode {} with search key {} already exists!".format(cn, key))
            return

        print("\t\tInsert a node with key {}".format(key))
        cn = self.root
        nn = BstNode(key)
        while cn:
            if key <= cn.key:
                if cn.left is None:
                    cn.left = nn
                    return
                cn = cn.left
            else:
                if cn.right is None:
                    cn.right = nn
                    return
                cn = cn.right

    def search(self, key):
        if self._sanity_check_failed():
            return False

        ret, node, parent = self._searchKey(key)
        return ret

    def delete(self, key):
        if self._sanity_check_failed():
            return
        
        pn, cn = None, self.root
        delRoot = True if cn.key == key else False
        print("\t\tDelete a node with key {}. Root node? {}".format(key, delRoot))
        '''
        Possibilities:
        1. root node or any node with left and right subtrees is deleted
           - Find the successor to occupy the place of the deleted node
           - Detach the successor from its current parent and attach it to the parent of the deleted node
           - Set the left, right pointers of the successor
           - If the root is deleted, set the successor as the new root
        2. leaf node gets deleted
           - Corresponding left/right child of the parent should be set to None 
        '''
        
        if not delRoot:
            ret, cn, pn = self._searchKey(key)
            if not ret:
                return

        # Find the successor
        assert cn is not None, "Node to be deleted should not be None"
        sn = self._getSuccessorNode(cn)
        
        # Update the pointer of the parent node to point to the successor node
        if pn is not None:
            if pn.left == cn:
                pn.left = sn
            else:
                pn.right = sn

        # Set the pointers of the successor node
        if sn is not None:
            print("\t\tSuccessor node {} with key {}".format(sn, sn.key))
            sn.left = cn.left if sn != cn.left else None
            sn.right = cn.right

        # Update root
        if delRoot:
            self.root = sn

        del cn

    # Inorder traversal wrapper function
    def inOrderTraversal(self, node):
        _divider()
        print("Inorder traversal:")
        inorder_traversal(node)
        _divider()

    # Pre-order traversal prints the keys in the order of current node and then its left and right children
    def preOrderTraversal(self, node):
        preorder_traversal(node)

    # Post order traversal prints the keys in the order of left, right children and then the current node
    def postOrderTraversal(self, node):
        postorder_traversal(node)


'''
Test code
'''
def _divider():
    print("\n====================================\n")

def _testInsert(bst):
    print("Inserting Nodes:")
    nodes = [50, 150, 25, 75, 125, 175, 15, 35, 65, 85, 115, 135, 165, 185]
    for n in nodes:
        bst.insert(n)
    bst.getSmallest()
    bst.getLargest()
    r = bst.getRoot()
    print("Inorder Traversal with root node {} after insertion:".format(r.key))    
    bst.inOrderTraversal(r)

def _testSearch(bst):
    snodes = [150, 45, 65, 95, 175]
    print("Searching Nodes:")
    for n in snodes:
        bst.search(n)
    _divider()

def _testDelete(bst):
    dnodes = [50, 150, 25, 75, 125, 175, 15, 100, 65, 85, 115, 135, 165, 185, 35]
    print("Deleting Nodes:")
    for n in dnodes:
        bst.delete(n)
        bst.getSmallest()
        bst.getLargest()
        r = bst.getRoot()
        print("Inorder Traversal with root node {} after deletion:".format(r.key if r else None))
        bst.inOrderTraversal(r)

bst = Bst(100)
_testInsert(bst)
_testSearch(bst)
_testDelete(bst)
