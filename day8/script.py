class Display:
    def __init__(self, x, y, file):
        self.width = x
        self.height = y
        self.array = [[0 for i in range(x)] for j in range(y)]
        self.data = file

    def createRectangle(self, x, y):
        for i in range(y):
            for j in range(x):
                self.array[i][j] = 1

    def rotateColumn(self, y, b):
        col = [self.array[i][y] for i in range(self.height)]
        col = col[-b:] + col[:-b]

        for i, row in enumerate(self.array):
            row[y] = col[i]

    def rotateRow(self, x, b):
        head = self.array[x][-b:]
        tail = self.array[x][:-b]
        self.array[x] = head + tail

    def draw(self):
        for line in self.array:
            for char in line:
                if char == 1:
                    print("#", end='')
                else:
                    print(" ", end='')
            print("")

    def countLit(self):
        counter = 0
        for row in self.array:
            for element in row:
                if element == 1:
                    counter += 1
        return counter

    def interpreteData(self):
        with open(self.data) as file:
            for line in file:
                line = line.strip("\n")

                if 'rect' in line:
                    x = line.split("x")[0].split(" ")[1]
                    y = line.split("x")[1]
                    self.createRectangle(int(x), int(y))
                elif 'row' in line:
                    y = line.split("=")[1].split(" ")[0]
                    b = line.split("by ")[1]
                    self.rotateRow(int(y), int(b))
                elif 'column' in line:
                    x = line.split("=")[1].split(" ")[0]
                    b = line.split("by ")[1]
                    self.rotateColumn(int(x), int(b))
                else:
                    print("wuut")


d = Display(50, 6, "data.txt")
d.interpreteData()

# Part 1
print(d.countLit())

# Part 2
d.draw()
