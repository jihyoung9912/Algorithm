from stack import Stack
from tree_node import TreeNode


class BTreeBuilder:
    @staticmethod
    def build(sexpr):
        stack_proc = Stack()
        stack_subtree = Stack()
        root = None
        for expr in sexpr:
            if expr != ")":
                stack_proc.push(TreeNode(expr))
                continue
            while stack_proc.peek().elem != "(":
                node = stack_proc.peek()
                stack_proc.pop()
                node = node if node.elem != "#" else None
                stack_subtree.push(node)
            stack_proc.pop()  # remove "(“
            if stack_proc.is_empty():
                root = stack_subtree.peek()
                stack_subtree.pop()
            else:
                root = stack_proc.peek()
                stack_proc.pop()
            if stack_subtree.is_empty():
                continue
                root.left_child = stack_subtree.peek()
                stack_subtree.pop()
                root.right_child = stack_subtree.peek()
                stack_subtree.pop()
                stack_proc.push(root)
            if not stack_proc.is_empty():
                raise Exception("expression is wrong.")
            return root


if __name__ == "__main__":
    sexpr = "( + ( * ( * ( / ( A B ) C ) D ) E ) )".split()
    root = BTreeBuilder.build(sexpr)
    print(root)  # +
    print(root.left_child)  # *
    print(root.right_child)  # E
    print(root.left_child.left_child)  # *
    print(root.left_child.right_child)  # D
    print(root.left_child.left_child.left_child)  # /
    print(root.left_child.left_child.right_child)  # C
    print(root.left_child.left_child.left_child.left_child)  # A
    print(root.left_child.left_child.left_child.right_child)  # B
