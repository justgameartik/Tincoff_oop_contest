class Stack():
    def __init__(self, link):
        self.values = []
        self.error = False
        self.file = link
    
    def add_num(self, value):
        self.values.append(value)

    def drop_num(self):
        self.values.pop()

    def swap_nums(self):
        temp = self.values[-1]
        self.values[-1] = self.values[-2]
        self.values[-2] = temp
    
    def dublicate(self):
        self.values.append(self.values[-1])

    def over(self):
        self.values.append(self.values[-2])

    def mathematic(self, type):
        num_2 = int(self.values.pop())
        num_1 = int(self.values.pop())
        if type == '+':
            self.__add(num_1, num_2)
        elif type == '-':
            self.__minus(num_1, num_2)
        elif type == '*':
            self.__mul(num_1, num_2)
        elif type == '/':
            self.__div(num_1, num_2)

    def __add(self, num_1, num_2):
        self.values.append(str(num_1 + num_2))
    
    def __minus(self, num_1, num_2):
        self.values.append(str(num_1 - num_2))

    def __mul(self, num_1, num_2):
        self.values.append(str(num_1 * num_2))

    def __div(self, num_1, num_2):
        self.values.append(str(num_1 // num_2))

    def read_command(self, line):
        try:
            if line.isdigit():
                self.add_num(line)
            elif line == "DROP":
                self.drop_num()
            elif line == "SWAP":
                self.swap_nums()
            elif line == 'DUP':
                self.dublicate()
            elif line == 'OVER':
                self.over()
            elif line in ['+', '-', '*', '/']:
                self.mathematic(line)
            elif line == '':
                self.__del__()
            else:
                self.error = True
        except:
            self.error = True

    def __del__(self):
        with open(self.file, 'w') as file:
            if self.error:
                file.write("ERROR")
            elif not self.values:
                file.write("EMPTY")
            else:
                file.write(' '.join(self.values))
            del self.values

stack = Stack('output.txt')
with open('input.txt', 'r') as file:
    lines = file.read().split('\n')
    for line in lines:
        stack.read_command(line.strip())
