class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_val(self):
        return self.val

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def set_val(self, val):
        self.val = val
