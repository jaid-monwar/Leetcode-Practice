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

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while(True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right




my_bst = BST()
my_bst.insert(2)
my_bst.insert(1)
my_bst.insert(3)

print(my_bst.root.value)        
print(my_bst.root.left.value)        
print(my_bst.root.right.value)        