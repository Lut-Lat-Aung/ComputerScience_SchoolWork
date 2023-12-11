
# ---- BS Tree -----

'''''
from BinarySearchTree import *

bst = BSTree()
a = [56,70,30,60,65,22,11,16,40,95,63,3,67]


for k in a:
    x = BST_Node(k)
    bst.Tree_Insert(x)
    
bst.Tree_Delete(x)
bst.print_BSTree()
#print(bst.Tree_Successor(BST_Node(67)))

'''
'''
bst2 = BSTree()
for k in range(1,11):
    x = BST_Node(k)
    bst2.Tree_Insert(x)

bst2.print_BSTree()
'''


# ---- RB Tree -----

from RedBlackTree import *

rbt = RBTree()
a = [12,3,11,15,7,10,13,14,6,4,17,8]

for k in a:
    x = RB_Node(k)
    rbt.RB_Insert(x)
rbt.print_RBTree()



    


