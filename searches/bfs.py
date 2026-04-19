import sys
import os
from collections import deque
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'datastructures'))
from tree_node import TreeNode

def breadth_first_search(node, target):
    if node is None:
        return False

    queue = deque([node])

    while queue:
        current_node = queue.popleft()
        if current_node.val == target:
            return True
        if current_node.left is not None:
            queue.append(current_node.left)
        if current_node.right is not None:
            queue.append(current_node.right)
    return False

# Example usage:
if __name__ == "__main__":
    # Constructing a sample binary tree:
    #         1
    #        / \
    #       2   3
    #      / \   \
    #     4   5.  6
    #       \      /
    #        7    8
    root = TreeNode(1)
    rl = TreeNode(2)
    root.set_left(rl)
    rr = TreeNode(3)
    root.set_right(rr)
    rl.set_left(TreeNode(4))
    rl.set_right(TreeNode(5))
    rr.set_right(TreeNode(6))
    rl.get_left().set_right(TreeNode(7))
    rr.get_right().set_left(TreeNode(8))

    target_nodes = [5, 7, 8, 9]
    for target in target_nodes:
        found = breadth_first_search(root, target)
        print(f"Element {target} {'found' if found else 'not found'} in the tree.")