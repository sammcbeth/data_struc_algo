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

    def BFS(self):
        data = []
        queue = []
        node = self.root
        queue.append(node)
        while queue:
            node = queue.pop(0)
            data.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return data
    
    

    
    def DFS_PreOrder(self):
        data = []
        current = self.root
        
        def traverse(node, data):
            data.append(node.val)
            if node.left:
                data = traverse(node.left, data)
            if node.right:
                data = traverse(node.right, data)
            return data
        data = traverse(current, data)
        return data
    
    def DFS_PostOrder(self):
        data = []
        current = self.root
        def traverse(node, data):
            if node.left:
                data = traverse(node.left, data)
            if node.right:
                data = traverse(node.right, data)
            data.append(node.val)
            return data
        data = traverse(current, data)
        return data
    
    def DFS_InOrder(self):
        data = []
        current = self.root
        def traverse(node, data):
            if node.left:
                data = traverse(node.left, data)
            data.append(node.val)
            if node.right:
                data = traverse(node.right, data)
            return data
        data = traverse(current, data)
        return data
    
   
        

    
tree = BinarySearchTree()
tree.insert(10)
tree.insert(6)
tree.insert(15)
tree.insert(3)
tree.insert(8)
tree.insert(20)

print(tree.BFS())
print(tree.DFS_PreOrder())
print(tree.DFS_PostOrder())
print(tree.DFS_InOrder())