class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_val:'int'):
        self.root = Node(root_val)
    
    def lca(self, p:'Node', q:'Node'):
        return self._lca(self.root, p, q)
    
    def _lca(self, curr_node:'Node', p:'Node', q:'Node'):
        if curr_node is None:
            return None
        
        if curr_node.value == p.value or curr_node.value == q.value:
            return curr_node
        
        left_subtree = self._lca(curr_node.left, p, q)
        right_subtree = self._lca(curr_node.right, p, q)
        
        if left_subtree is None: return right_subtree
        if right_subtree is None: return left_subtree
        
        return curr_node

def lca(p:'Node', q:'Node'):
    print('LCA of node {} and {} is {}'.format(p.value, q.value, t.lca(p, q).value))

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

lca(r.left, r.right)                            # 5, 1 => 3
lca(r.left.left, r.left.right.right)            # 6, 4 => 5
lca(r.right, r.right.left)                      # 1, 0 => 1
lca(r.left.right.left, r.left.right.right)      # 7, 4 => 2
