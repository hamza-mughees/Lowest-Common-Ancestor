import unittest
from dag_lca import Node, DAG

dag = DAG(0)
r = dag.root

n1, n2, n3, n4, n5 = Node(1), Node(2), Node(3), Node(4), Node(5)

r.descendants = [n1]
n1.ancestors = [r]
n1.descendants = [n2, n3, n4, n5]
n2.ancestors = [n1]
n2.descendants = [n3, n4]
n3.ancestors = [n1, n2]
n4.ancestors = [n1, n2]
n4.descendants = [n5]
n5.ancestors = [n1, n4]

'''
An image (PNG) of the graph created above accompanies the code
'''

class TestLCA(unittest.TestCase):
    def test0(self):
        self.assertEqual(dag.lca(n2, n5), n1)
    
    def test1(self):
        self.assertEqual(dag.lca(n1, n2), n1)
    
    def test2(self):
        self.assertEqual(dag.lca(n5, n3), n1)
    
    def test3(self):
        self.assertEqual(dag.lca(n3, n4), n2)
    
