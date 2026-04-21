import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'datastructures'))
from tree_node import TreeNode

def inorder_traversal(root):
    if not root:
        return []
    inorder_traversal(root.left)
    print(f"Visiting node with key: {root.key}")
    inorder_traversal(root.right)

def preorder_traversal(root):
    if not root:
        return []
    print(f"Visiting node with key: {root.key}")
    preorder_traversal(root.left)
    preorder_traversal(root.right)

def postorder_traversal(root):
    if not root:
        return []
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(f"Visiting node with key: {root.key}")

if __name__ == "__main__":
    # Constructing a sample binary tree:
    #         1
    #        / \
    #       2   3
    #      / \   \
    #     4   5.  6
    root = TreeNode(1)
    rl = TreeNode(2)
    root.set_left(rl)
    rr = TreeNode(3)
    root.set_right(rr)
    rl.set_left(TreeNode(4))
    rl.set_right(TreeNode(5))
    rr.set_right(TreeNode(6))

    # Perform inorder traversal
    print("Inorder Traversal:")
    inorder_traversal(root) 
    # Perform preorder traversal
    print("Preorder Traversal:")
    preorder_traversal(root)
    # Perform postorder traversal
    print("Postorder Traversal:")
    postorder_traversal(root)