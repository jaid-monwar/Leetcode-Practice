class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    # For a BST with a root node
    def __init__(self, value):
        new_node = Node(value)
        self.root = new_node

    # For an empty BST
    def __init__(self):
        self.root = None



my_bst = BST()

print(my_bst.root)        