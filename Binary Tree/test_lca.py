import unittest
from lca import Node, BinaryTree

def constructTree():
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

    return t, r

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

t, r = constructTree()

class TestLCA(unittest.TestCase):
    def test_lca_5_1(self):
        # 5, 1 => 3
        self.assertEqual(t.lca(r.left, r.right), r)
    
    def test_lca_6_4(self):
        # 6, 4 => 5
        self.assertEqual(t.lca(r.left.left, r.left.right.right), r.left)
    
    def test_lca_1_0(self):
        # 1, 0 => 1
        self.assertEqual(t.lca(r.right, r.right.left), r.right)
    
    def test_lca_7_4(self):
        # 7, 4 => 2
        self.assertEqual(t.lca(r.left.right.left, r.left.right.right), r.left.right)
