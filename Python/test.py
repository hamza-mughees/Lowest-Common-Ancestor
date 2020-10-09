from node import Node
from binary_tree import BinaryTree

t = BinaryTree(3)
r = t.root

r.left = Node(5)
r.right = Node(1)
r.left.left = Node(6)
r.left.right = Node(2)
r.right.left = Node(0)
r.right.right = Node(8)
r.left.right.left = Node(7)
r.left.right.right = Node(4)

'''
The above code generates the following tree:
            3
          /   \
        5       1
       / \     / \
      6   2   0   8
         / \
        7   4
'''

def lca(p:'Node', q:'Node'):
    print('LCA of node {} and {} is {}'.format(p.value, q.value, t.lca(p, q).value))

lca(r.left, r.right)                            # 5, 1 => 3
lca(r.left.left, r.left.right.right)            # 6, 4 => 5
lca(r.right, r.right.left)                      # 1, 0 => 1
lca(r.left.right.left, r.left.right.right)      # 7, 4 => 2
