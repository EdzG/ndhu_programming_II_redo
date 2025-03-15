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

triangles = []

while True:
    try:
        user_input  = list(input().split())
        if int(user_input[0]) == 1:
            t = Triangle(*map(float, user_input[1:]))
            triangles.append(t.area())
        elif int(user_input[0]) == 2:
            t = Triangle(*map(float, user_input[1:]))
            triangles.append(t.area())
        else:
            break
    except KeyboardInterrupt:
        break

triangles.sort()
for triangle in triangles:
    print(triangle)




