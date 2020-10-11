class Node(val value: Int) {
    var left: Node? = null
    var right: Node? = null
}

class BinaryTree(root_val: Int) {
    val root: Node = Node(root_val)

    fun lca(p: Node, q: Node): Node? {
        return this._lca(this.root, p, q)
    }

    fun _lca(curr_node: Node?, p: Node, q: Node): Node? {
        if (curr_node == null) return null

        if (curr_node.value.equals(p.value) or curr_node.value.equals(q.value)) return curr_node

        var left_subtree = this._lca(curr_node.left, p, q)
        var right_subtree = this._lca(curr_node.right, p, q)

        if (left_subtree == null) return right_subtree
        if (right_subtree == null) return left_subtree

        return curr_node
    }
}

fun lca(t: BinaryTree, p: Node, q: Node) {
    println("LCA of node ${p.value} and ${q.value} is ${t.lca(p, q)?.value}")
}

fun main() {
    var t = BinaryTree(3)

    t.root.left = Node(5)
    t.root.right = Node(1)
    t.root.left?.left = Node(6)
    t.root.left?.right = Node(2)
    t.root.right?.left = Node(0)
    t.root.right?.right = Node(8)
    t.root.left?.right?.left = Node(7)
    t.root.left?.right?.right = Node(4)

    lca(t, t.root.left!!, t.root.right!!)                                   // 5, 1 => 3
    lca(t, t.root.left!!.left!!, t.root.left!!.right!!.right!!)             // 6, 4 => 5
    lca(t, t.root.right!!, t.root.right!!.left!!)                           // 1, 0 => 1
    lca(t, t.root.left!!.right!!.left!!, t.root.left!!.right!!.right!!)     // 7, 4 => 2
}
