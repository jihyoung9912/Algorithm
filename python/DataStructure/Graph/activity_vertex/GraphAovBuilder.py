import HeadNode, Node


class GraphAovBuilder:
    @staticmethod
    def build(mat):
        if not mat:
            raise Exception("the mat should not be none.")
        size = len(mat)
        # Node(i) 는 Adjacency list 의 head 이다.
        list_ = [HeadNode(i) for i in range(size)]

        for row in range(size):
            prev = list_[row]
            for col in range(size):
                if not mat[row][col]:
                    continue
                node = Node(col)
                prev.link = node
                prev = node
        return list_