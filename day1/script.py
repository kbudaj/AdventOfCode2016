class Start():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.head = "up"
        self.history = []
        self.firstDouble = ()

    def get(self):
        return self.x, self.y

    def checkFirst(self, x, y):
        if self.firstDouble == ():
            pos = (x, y)
            if pos in self.history:
                self.firstDouble = pos
            else:
                self.history.append(pos)

    def moveLeft(self, distance):
        if self.head == "up":
            for i in range(0, distance):
                self.x -= 1
                self.checkFirst(self.x, self.y)
            self.head = "left"

        elif self.head == "down":
            for i in range(0, distance):
                self.x += 1
                self.checkFirst(self.x, self.y)
            self.head = "right"

        elif self.head == "left":
            for i in range(0, distance):
                self.y -= 1
                self.checkFirst(self.x, self.y)
            self.head = "down"

        elif self.head == "right":
            for i in range(0, distance):
                self.y += 1
                self.checkFirst(self.x, self.y)
            self.head = "up"

    def moveRight(self, distance):
        if self.head == "up":
            for i in range(0, distance):
                self.x += 1
                self.checkFirst(self.x, self.y)
            self.head = "right"

        elif self.head == "down":
            for i in range(0, distance):
                self.x -= 1
                self.checkFirst(self.x, self.y)
            self.head = "left"

        elif self.head == "left":
            for i in range(0, distance):
                self.y += 1
                self.checkFirst(self.x, self.y)
            self.head = "up"

        elif self.head == "right":
            for i in range(0, distance):
                self.y -= 1
                self.checkFirst(self.x, self.y)
            self.head = "down"





class Position():
    def __init__(self, x, y):
        self.x = x
        self.y = y

start = Start()

ar = ["L1", "R3", "R1", "L5", "L2", "L5", "R4", "L2", "R2", "R2", "L2", "R1", "L5", "R3", "L4", "L1", "L2", "R3", "R5", "L2", "R5", "L1", "R2", "L5", "R4", "R2", "R2", "L1", "L1", "R1", "L3", "L1", "R1", "L3", "R5", "R3", "R3", "L4", "R4", "L2", "L4", "R1", "R1", "L193", "R2", "L1", "R54", "R1", "L1", "R71", "L4", "R3", "R191", "R3", "R2", "L4", "R3", "R2", "L2", "L4", "L5", "R4", "R1", "L2", "L2", "L3", "L2", "L1", "R4", "R1", "R5", "R3", "L5", "R3", "R4", "L2", "R3", "L1", "L3", "L3", "L5", "L1", "L3", "L3", "L1", "R3", "L3", "L2", "R1", "L3", "L1", "R5", "R4", "R3", "R2", "R3", "L1", "L2", "R4", "L3", "R1", "L1", "L1", "R5", "R2", "R4", "R5", "L1", "L1", "R1", "L2", "L4", "R3", "L1", "L3", "R5", "R4", "R3", "R3", "L2", "R2", "L1", "R4", "R2", "L3", "L4", "L2", "R2", "R2", "L4", "R3", "R5", "L2", "R2", "R4", "R5", "L2", "L3", "L2", "R5", "L4", "L2", "R3", "L5", "R2", "L1", "R1", "R3", "R3", "L5", "L2", "L2", "R5"]

for move in ar:
    if "L" in move:
        distance = move.split("L")[1]
        start.moveLeft(int(distance))
    elif "R" in move:
        distance = move.split("R")[1]
        start.moveRight(int(distance))

x, y = start.get()

# Part 1
print(abs(x)+abs(y))
dX = start.firstDouble[0]
dY = start.firstDouble[1]

# Part 2
print(abs(dX)+abs(dY))
