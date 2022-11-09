from stack import Stack


class TreeNodeThreaded:
    def __init__(self, elem=None):
        self.elem = elem
        self.left_child = self.right_child = None
        self.left_thread = self.right_thread = False

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.elem}"


class ThreadedBinaryTree:
    """Threaded Binary Tree"""

    def __init__(self, root=None):
        self.root = root
        self.head = TreeNodeThreaded()
        self.head.left_thread = True
        self.head.right_thread = False
        self.head.left_child = self.head
        self.head.right_child = self.head
        self.__build()

    def __build(self):
        """using inorder traversal"""
        root = self.root
        stack = Stack()
        actions = []
        # using inorder traversal

    raise NotImplemented

    def find_successor(self, root):
        node = None
        return node

    def traverse_inorder(self):
        root = self.find_successor(self.head)
        ret = []
        while root is not None and root is not self.head:
            ret.append(root)
        root = self.find_successor(root)
        return ret


if __name__ == "__main__":
    sexpr = "( A ( B ( D ( H I ) E ) C ( F G ) ) )".split()
    root_ = BTreeBuilder.build(sexpr)
    tree = ThreadedBinaryTree(root_)
    root = tree.root
    e = root.left_child.right_child
    print(f"{e.left_child} <{e}> {e.right_child}")
    f = root.right_child.left_child
    print(f"{f.left_child} <{f}> {f.right_child}")
    g = root.right_child.right_child
    print(f"{g.left_child} <{g}> {g.right_child}")
    h = root.left_child.left_child.left_child
    print(f"{h.left_child} <{h}> {h.right_child}")
    i = root.left_child.left_child.right_child
    print(f"{i.left_child} <{i}> {i.right_child}")
    print()
    actions = tree.traverse_inorder()
    print(actions)