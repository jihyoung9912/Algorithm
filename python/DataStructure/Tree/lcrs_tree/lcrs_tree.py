from stack import Stack


class Tree:
    def __init__(self):
        self.root = None

    def build(self, sexpr):
        stack = Stack()
        it = iter(sexpr)

        root = None
        while stack.is_empty() or it:
            try:
                token = next(it)
            except StopIteration:
                break

            if token != ")":
                stack.push(TreeNode(token))
                continue

            prev = None
            while stack.peek().elem != "(":
                node = stack.peek()
                stack.pop()
                node.right_sibling = prev
                prev = node

            stack.pop()

            if stack.is_empty():
                root = prev
                continue

            root = stack.peek()
            root.left_child = prev
            stack.pop()
            stack.push(root)

        if not stack.is_empty():
            raise Exception("expression is wrong.")

        self.root = root


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
# b = root.left_child
# print(b)
# e = b.left_child
# print(e)
# k = e.left_child
# print(k)
# l = k.right_sibling
# print(l)
# f = e.right_sibling
# print(f)
# c = b.right_sibling
# print(c)
# d = c.right_sibling
# print(d)
# g = c.left_child
# print(g)
# h = d.left_child
# print(h)
# i = h.right_sibling
# print(i)
# j = i.right_sibling
# print(j)

# degree : 자식노드 개수, 차수
# depth : root node에서 나까지
# height : leaf node에서 나까지
# degree of tree : 최대 자식노드 개수 (degree 최대값)
# size of tree : tree를 구성하고 있는 node 개수
# height of tree : 최대 나에서 leaf node까지
# leaf node : degree가 0인 node (자식이 없는 node)
# internal node : degree가 0 이상인 node (자식을 가진 node)
# parent : 부모
# child : 자식
# sibling : 형제
# ancestor : root node까지의 path에 존재하는 node들
# descendent : 자손(leaf node까지), 자식과 헷갈리지 말 것
# level : node가 존재하는 층
# waisting memory
# k = degree of the tree, n = size of the tree
# n(k-1) + 1 // if n = 13, k = 3 --> 27
