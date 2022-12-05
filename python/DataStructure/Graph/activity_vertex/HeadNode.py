class HeadNode:
    def __init__(self, id_=0, indegree=0):
        self.id_ = id_
        self.indegree = indegree
        self.link = None

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.id_}"
