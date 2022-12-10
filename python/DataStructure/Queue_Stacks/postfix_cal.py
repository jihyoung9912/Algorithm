from stacks import Stack


class Postfix:
    OPS = "+", "-", "*", "/"

    def __init__(self, expr):
        self.expr = expr

    def evaluate(self):
        stack = Stack(len(self.expr))
        ret = 0
        tmp = expr.split(' ')

        for i in tmp:
            if i in self.OPS:
                tok_2 = int(stack.peek())
                stack.pop()
                tok_1 = int(stack.peek())
                stack.pop()
                ret = self.cal(tok_1, tok_2, i)
                stack.push(ret)

            elif i not in self.OPS:
                stack.push(i)
        return ret

    def cal(self, tok_1, tok_2, op):
        if op == "+":
            return tok_1 + tok_2
        if op == "-":
            return tok_1 - tok_2
        if op == "*":
            return tok_1 * tok_2
        if op == "/":
            return tok_1 / tok_2
        raise Exception("Unknown operator.")

    def __str__(self):
        return self.expr


if __name__ == "__main__":
    expr = "4 10 2 + * 7 -"

    postfix = Postfix(expr)
    print("Expression:", postfix)
    res = postfix.evaluate()
    print("Caculation:", res)
