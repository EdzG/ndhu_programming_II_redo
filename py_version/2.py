class Point: 
    def __init__(self, x, y):
        self._x = x
        self._y = y
    def display(self):
        print(f"({self._x}, {self._y})")
    def setX(self, x):
        self._x = x
    def setY(self, y):
        self._y = y
    def getX(self):
        return self._x
    def getY(self):
        return self._y
class Segment:
    def __init__(self, start, end):
        self._start = start
        self._end = end
    def distance(self):
        return ((self._end.getX() - self._start.getX())**2 + (self._end.getY() - self._start.getY())**2)**0.5

numOfPoints = int(input())

for i in range(numOfPoints):
    x, y, x1, y1 = map(float, input().split())
    seg = Segment(Point(x, y), Point(x1, y1))
    print(f"{seg.distance():.4f}")