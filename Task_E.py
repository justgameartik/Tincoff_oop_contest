class Graph():
    def __init__(self, link):
        self.matrix = []
        self.file_name = link

    def read_from_file(self, file_name=None):
        if file_name:
            with open(file_name) as file:
                self.size = int(file.readline().strip())
                self.matrix = [[0 for _ in range(self.size)] 
                               for __ in range(self.size)]
                for i in range(self.size):
                    line = file.readline().strip().split()
                    for j in range(self.size):
                        self.matrix[i][j] = int(line[j])

    def save_adjacency_lists(self, file_name):
        self.read_from_file(self.file_name)
        with open(file_name, "w") as file:
            for line in self.matrix:
                if sum(line) == 0:
                    file.write("0")
                else:
                    for i, number in enumerate(line):
                        if number == 1:
                            file.write(f"{i+1} ")
                file.write("\n")


a = Graph('input.txt')
a.save_adjacency_lists("output.txt")
