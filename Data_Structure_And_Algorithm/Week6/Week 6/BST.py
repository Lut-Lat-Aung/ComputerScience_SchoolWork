import sys
sys.setrecursionlimit(10001)

root = None
        

class node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.p = None
        self.left = None
        self.right = None


def Inorder_Tree_Walk(x):
    if x != None:
        Inorder_Tree_Walk(x.left)
        print(x.key)
        Inorder_Tree_Walk(x.right)


def Tree_Minimum(x):
    # Replace "pass" with your code
    while x.left != None:
        x = x.left
    return x

def Tree_Maximum(x):
    # Replace "pass" with your code
    while x.right != None:
        x = x.right
    return x

def Tree_Successor(x):
    # Replace "pass" with your code
    if x.right != None:
        return Tree_Minimum(x.right)
    y = x.p
    while y != None and x == y.right:
        x = y
        y = y.p
    return y

'''
Adding your own Tree_Predecessor(x) is recommended, but not required
'''

def Transplant(u, v):
    # This function is required for supporting Tree_Delete
    # Replace "pass" with your code
    if u.p == None:
        root = v

    elif u == u.p.left:
        u.p.left = v

    else:
        u.p.right = v
    
    if v!= None:
        v.p = u.p


def Tree_Delete(z):
    # Replace "pass" with your code
    if z.left  == None:
        Transplant(z,z.right)
    elif z.right == None:
        Transplant(z,z.left)
    else:
        y = Tree_Minimum(z.right)

        if y.p != z:
            Transplant(y,y.right)
            y.right = z.right
            y.right.p = y
        Transplant(z,y)
        y.left = z.left
        y.left.p = y

def Tree_Search(k):
    x = root

    # Replace "pass" with your code
    while x != None and k != x.key:
        if k < x.key:
            x = x.left

        else:
            x = x.right
    return x

def Tree_Insert(z):
    global root
    

    # Replace "pass" with your code
    y = None
    x = root
    while x!= None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right

    z.p = y
    if y == None:
        root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z

# Function to print
def printCall ( node , indent , last ) :
    if node != None :
        print(indent, end=' ')
        if last :
            print ("R----",end= ' ')
            indent += "     "
        else :
            print("L----",end=' ')
            indent += "|    "

        print ( str ( node.key ) )
        printCall ( node.left , indent , False )
        printCall ( node.right , indent , True )

# Function to call print
def print_BSTree (root) :
    printCall( root , "" , True )



# Create the root node
root = node(30, None)

# Insert nodes into the BST
Tree_Insert(node(20, None))
Tree_Insert(node(67, None))
Tree_Insert(node(63, None))




# Print the BST
print("Binary Search Tree:")
print_BSTree(root)
print()

print(Tree_Successor(node(67, None)))
print(Tree_Maximum(root).key)
print(Tree_Minimum(root).key)

print()
