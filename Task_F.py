class Graph():
    def __init__(self, size):
        self.adjacency_list = []
        self.adjacency_matrix = [[0 for _ in range(size)] for __ in range(size)]

    def read_list(self, line):
        self.adjacency_list.append([int(i) for i in line.split()])

    def __build_adjacency_matrix(self):
        for i in range(len(self.adjacency_list)):
            for way in self.adjacency_list[i]:
                if way == 0:
                    continue
                self.adjacency_matrix[i][way - 1] = 1

    def print_matrix(self):
        self.__build_adjacency_matrix()
        for line in self.adjacency_matrix:
            for col in line:
                print(col, end= ' ')
            print()

n = int(input())
graph = Graph(n)
for i in range(n):
    line = input()
    graph.read_list(line)

graph.print_matrix()
