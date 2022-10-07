from stacks import Stack

class Postfix:
    OPS = "+", "-", "*", "/"

    def __init__(self, expr):
        self.expr = expr

    def evaluate(self):
        # stack = Stack(len(self.expr))
        stack = len(self.expr)
        ret = 0
        list_ = []
        for i in self.expr:
            if i != ' ':
                list_.append(i)
                self.cal(list_)

        return list_

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

    def __len__(self):
        return len(self.expr)


if __name__ == "__main__":
    expr = "4 10 2 + * 7 -"

    postfix = Postfix(expr)
    print("Expression:", postfix)
    print(postfix.evaluate())
    # res = postfix.evaluate()
    # print("Caculation:", res)
