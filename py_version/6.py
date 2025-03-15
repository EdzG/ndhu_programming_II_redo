import sys
class Triangle:
    def __init__(self, *args):
        if len(args) == 3:
            self._sideA, self._sideB, self._sideC = args
        elif len(args) == 6:
            x1, y1, x2, y2, x3, y3 = args
            self._sideA = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
            self._sideB = ((x3 - x2)**2 + (y3 - y2)**2)**0.5
            self._sideC = ((x3 - x1)**2 + (y3 - y1)**2)**0.5
        else:
            raise ValueError("Invalid number of arguments")
    def area(self):
        s = (self._sideA + self._sideB + self._sideC) / 2
        area = (s*(s - self._sideA) * (s - self._sideB) * (s - self._sideC))**0.5
        return area; 

while True:
    try:
        type = int(input()) 
        if type == 1:
            a, b, c = map(float, input().split())
            t = Triangle(a, b, c)
            print(t.area())
        elif type == 2:
            x1, y1, x2, y2, x3, y3 = map(float, input().split())
            t = Triangle(x1, y1, x2, y2, x3, y3)
            print(t.area()) 
        
    except KeyboardInterrupt:
        break



