class TreeNode:
    def __init__(self, key=0, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_key(self):
        return self.key

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def set_key(self, key):
        self.key = key
