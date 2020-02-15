class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        pointer = self.root
        if not pointer:
            self.root = Node(val)
            return self
        while True:
            if val < pointer.val:
                if not pointer.left:
                    pointer.left = Node(val)
                    break
                else:
                    pointer = pointer.left
            else:
                if not pointer.right:
                    pointer.right = Node(val)
                    break
                else:
                    pointer = pointer.right
        pointer = Node(val)



tree = BinarySearchTree()
tree.root = Node(10)
tree.root.right = Node(15)  
tree.root.left = Node(7)  
tree.root.left.right = Node(9)
tree.insert(4)
tree.insert(8)
print(tree.root.left.val)
print(tree.root.right.val)
print(tree.root.left.right.left.val)