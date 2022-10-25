from stack import Stack


class Tree:
    def __init__(self):
        self.root = None

    def build(self, sexpr):
        raise NotImplemented


class TreeNode:
    def __init__(self, elem):
        self.elem = elem
        self.left_child = None
        self.right_sibling = None

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.elem}"

sexpr = "( A ( B ( E ( K L ) F ) C ( G ) D ( H ( M ) I J ) ) )"
sexpr = sexpr.split()
tree = Tree()
tree.build(sexpr)
root = tree.root
print(root)
b = root.left_child
print(b)
e = b.left_child
print(e)
k = e.left_child
print(k)
l = k.right_sibling
print(l)
f = e.right_sibling
print(f)
c = b.right_sibling
print(c)
d = c.right_sibling
print(d)
g = c.left_child
print(g)
h = d.left_child
print(h)
i = h.right_sibling
print(i)
j = i.right_sibling
print(j)