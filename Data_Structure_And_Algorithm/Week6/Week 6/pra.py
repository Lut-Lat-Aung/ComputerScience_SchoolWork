import sys
sys.setrecursionlimit(10001)

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.p = None
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def inorder_tree_walk(self, x):
        if x is not None:
            self.inorder_tree_walk(x.left)
            print(x.key)
            self.inorder_tree_walk(x.right)

    def tree_minimum(self, x):
        while x.left is not None:
            x = x.left
        return x

    def tree_maximum(self, x):
        while x.right is not None:
            x = x.right
        return x

    def tree_successor(self, x):
        if x.right is not None:
            return self.tree_minimum(x.right)
        y = x.p
        while y is not None and x == y.right:
            x = y
            y = y.p
        return y

    def transplant(self, u, v):
        if u.p is None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v is not None:
            v.p = u.p

    def tree_delete(self, z):
        if z.left is None:
            self.transplant(z, z.right)
        elif z.right is None:
            self.transplant(z, z.left)
        else:
            y = self.tree_minimum(z.right)
            if y.p != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y

    def tree_search(self, k):
        x = self.root
        while x is not None and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def tree_insert(self, z):
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.p = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def print_call(self, node, indent, last):
        if node is not None:
            print(indent, end=' ')
            if last:
                print("R----", end=' ')
                indent += "     "
            else:
                print("L----", end=' ')
                indent += "|    "

            print(str(node.key))
            self.print_call(node.left, indent, False)
            self.print_call(node.right, indent, True)

    def print_tree(self):
        print("Binary Search Tree:")
        self.print_call(self.root, "", True)

# Example usage:
if __name__ == "__main__":
    bst = BST()

    # Insert nodes into the BST
    bst.tree_insert(Node(30, "Root Node"))
    bst.tree_insert(Node(20, "Node 20"))
    bst.tree_insert(Node(10, "Node 10"))

    # Print the BST
    bst.print_tree()

    print("Inorder Tree Walk:")
    bst.inorder_tree_walk(bst.root)

    # Find the minimum and maximum nodes
    min_node = bst.tree_minimum(bst.root)
    max_node = bst.tree_maximum(bst.root)

    print("Minimum Node:", min_node.key)
    print("Maximum Node:", max_node.key)

    # Delete a node from the BST
    node_to_delete = bst.tree_search(20)
    if node_to_delete:
        bst.tree_delete(node_to_delete)

    print("BST after deleting Node 20:")
    bst.print_tree()

    # Find the successor of a node
    successor_node = bst.tree_successor(bst.tree_search(10))
    if successor_node:
        print("Successor Node of 10:", successor_node.key)
    else:
        print("No successor found for Node 10.")
