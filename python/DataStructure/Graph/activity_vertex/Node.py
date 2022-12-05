class Node:
    def __init__(self, vertex=0):
        self.vertex = vertex
        self.link = None

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.vertex}"
