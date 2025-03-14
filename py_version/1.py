class Point: 
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def display(self):
        print(f"({self.x}, {self.y})")

numOfPoints = int(input())

for i in range(numOfPoints):
    x, y = input().split()
    point = Point(x, y)
    point.display()
