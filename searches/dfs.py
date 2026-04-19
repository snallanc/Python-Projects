import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'datastructures'))
from tree_node import TreeNode

def depth_first_search(node, target):
    if node is None:
        return False
    if node.val == target:
        return True
    return depth_first_search(node.left, target) or depth_first_search(node.right, target)

# Example usage:
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

    target = 5
    found = depth_first_search(root, target)
    print(f"Element {target} {'found' if found else 'not found'} in the tree.")
    target = 7
    found = depth_first_search(root, target)
    print(f"Element {target} {'found' if found else 'not found'} in the tree.")