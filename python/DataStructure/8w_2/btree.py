from stack import Stack


class TreeNode:
    def __init__(self, elem):
        self.elem = elem
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.elem}"


class BTree:
    def __init__(self):
        self.root = None

    def build(self, sexpr):
        stack = Stack()
        raise NotImplemented















# Tree에서 lcrs의 경우 siblings의 순서는 전혀 상관 없음
# Complete binary tree? 꽉 차진 않지만 순서대로 봤을 때 빠진 곳이 없음. 중간을 뛰어넘지 않고 순서대로 배열된 경우.
# full binary tree?다 두개씩 가진 꽉 참. 포화 이진 트리
# 15p
# 1. Full O Com O
# 2. Full x Com x
# 3. Full x Com o (순서는 무조건 좌측)
# 4. Full o Com o
# 5. Full x Com x
# 6. Full x Com o