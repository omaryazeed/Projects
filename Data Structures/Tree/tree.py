class Node:
    def __init__(self, key, l_child=None, r_child=None):
        self.key  = key
        self.right = r_child
        self.parent = None
        if r_child:
            self.right.parent = self
        self.left  = l_child
        if l_child:
            self.left.parent = self
    def __str__(self):
        return str(self.key)
class Tree:
    """
    This class implements the binary tree data structure along with operations on it
    """
    def __init__(self, root, l_child=None, r_child=None):
        self.root = root
        self.parent = None
        if l_child:
            if isinstance(l_child, Tree):
                self.root.left = l_child.root
                
            elif isinstance(l_child, Node):
                self.root.left = l_child
            self.root.left.parent = self.root
        if r_child:
            if isinstance(r_child, Tree):
                self.root.right = r_child.root
            elif isinstance(r_child, Node):
                self.root.right = r_child   
            self.root.right.parent = self.root

    def bfs(self):
        current = self.root
        s = []
        done = False
        elements = []
        while not done:
            elements.append(current.key)
            if current.left:
                s.append(current.left)
            if current.right:
                s.append(current.right)
            if s:
                current = s.pop(0)
            else:
                done = True      
        return str(elements)
    def preorder(self,node):
        if node is None:
            return
        print(node)
        preorder(node.left)
        preorder(node.right)
    def inorder(self,node):
        if node is None:
            return
        inorder(node.left)
        print(node)
        inorder(node.right)
    def postorder(self,node):
        if node is None:
            return
        postorder(node.left)
        postorder(node.right)
        print(node)
    def search(self, k, node):
        if node is None or node.key == k:
            return node
        if node.key > k:
            return self.search(k, node.left)
        return self.search(k, node.right)
    def search_nr(self,k):
        node = self.root
        while node:
            if node.key > k:
                node = node.left
            elif node.key < K:
                node = node.right
            else:
                return node
        return node
    def min(self, node):
        if node.left:
            return min(node.left)
        return node.key 
    def min_nr(self, node):
        while node.left:
            node = node.left
        return node.key 
    def max(self, node):
        if node.right:
            return min(node.right)
        return node.key 
    def max_nr(self, node):
        while node.right:
            node = node.right
        return node.key 
    def successor(self, node):

        if node.right:
            node = node.right
            while node.left:
                node = node.left
            successor = node
        else:
            successor_value = float("inf")
            successor = node
            key_value = node.key
            while node.parent:
                node = node.parent
                if node.key > key_value and node.key < successor_value:
                    successor = node
                    successor_value = node.key
        return successor
    def predecessor(self, node):

        if node.left:
            node = node.left
            while node.right:
                node = node.right
            successor = node
        else:
            successor_value = float("-inf")
            successor = node
            key_value = node.key
            while node.parent:
                node = node.parent
                if node.key < key_value and node.key > successor_value:
                    successor = node
                    successor_value = node.key

        return successor






rchild = Tree(Node(18), Node(17), Node(20))
lchild = Tree(Node(6), Tree(Node(3), Node(2), Node(4)), Tree(Node(7), None, Node(13, Node(9))))
tree = Tree(Node(15), lchild, rchild)
root = tree.root
node = tree.search(7, root)
print(tree.bfs())
print(tree.successor(node))
