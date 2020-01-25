class BstNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class Bst:
    def __init__(self, rootKey):
        self.root = BstNode(rootKey)

    def __sanity_check_failed(self):
        if not self.root:
            print("Tree is not initialized yet!")
            return True
        return False

    def getRoot(self):
        return self.root

    def insert(self, key):
        if self.__sanity_check_failed():
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
        if self.__sanity_check_failed():
            return
        cn = self.root
        while cn:
            if key == cn.key:
                print("Node {} with search key {} found!".format(cn, key))
                return cn
            elif key < cn.key:
                cn = cn.left
            else:
                cn = cn.right
        print("Node {} with search key {} is not found!".format(cn, key))
        return None

    def __get_successor_node(self, node):
        '''
        Successor will be the right most node of the left subtree
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
        
    def delete(self, key):
        if self.__sanity_check_failed():
            return
        
        pn, cn = None, self.root
        delRoot = True if cn.key == key else False
        print("Delete a node with key {} root node? {}".format(key, delRoot))
        '''
        Possibilities:
        1. root node or any node with left and right subtrees is deleted
           - Make the righmost node in the left subtree as next parent/root  
        2. leaf node gets deleted
           - node.left/right can be set to None w/o any adjustments 
        '''
        
        if not delRoot:
            pn = cn
            cn = cn.left if key <= cn.key else cn.right
            while cn:
                if key == cn.key:
                    break
                elif key < cn.key:
                    pn = cn
                    cn = cn.left
                else:
                    pn = cn
                    cn = cn.right
                
        if not cn:
            print("Node with key {} doesn't exist".format(key))
            return
        print("Node {} with key {} to be deleted is found".format(cn, key))

        # If we are here, then the node with the given key exists
        sn = self.__get_successor_node(cn)
        
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

    def preOrderTraversal(self, node):
        if not node:
            return
        print("{}".format(node.key))
        if node.left:
            self.preOrderTraversal(node.left)
        if node.right:
            self.preOrderTraversal(node.right)
        
# Test code
bst = Bst(100)
nodes = [50, 150, 25, 75, 125, 175, 15, 35, 65, 85, 115, 135, 165, 185]
for n in nodes:
    bst.insert(n)
    
bst.preOrderTraversal(bst.getRoot())
print("")

snodes = [150, 45, 65, 95, 175]
for n in snodes:
    bst.search(n)

dnodes = [50, 15, 100, 125]
for n in dnodes:
    bst.delete(n)
    bst.preOrderTraversal(bst.getRoot())
    print("")
