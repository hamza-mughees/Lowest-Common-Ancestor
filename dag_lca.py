class Node:
    def __init__(self, value):
        self.value = value
        self.ancestors = []
        self.descendants = []

class DAG:
    def __init__(self, root_val:'int'):
        self.root = Node(root_val)
    
    def lca(self, p:'Node', q:'Node'):
        if self.root.value == p.value or self.root.value == q.value:
            return self.root
        
        if p.value == q.value:
            return p
        
        comm_anc = []

        p_anc = p.ancestors
        q_anc = q.ancestors

        for anc_of_p in p_anc:
            for anc_of_q in q_anc:
                if anc_of_p.value == anc_of_q.value:
                    comm_anc.append(anc_of_p)
                    break
        
        if not comm_anc:
            if p.value > q.value:
                comm_anc.append(self.lca(p.ancestors[0], q))
            else:
                comm_anc.append(self.lca(p, q.ancestors[0]))
        
        return comm_anc[-1]
