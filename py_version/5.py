class Frog:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def moveLeft(self):
        self.x -= 1
    def moveRight(self):
        self.x += 1
    def moveUp(self):
        self.y += 1
    def moveDown(self):
        self.y -= 1
    def getCurrentPositionX(self):
        return self.x
    def getCurrentPositionY(self):
        return self.y
    def displayCurrentPosition(self):
        print(f"({self.x}, {self.y})")

x, y, dist_x, dist_y = map(int, input().split())
frog = Frog(x, y)
while (frog.getCurrentPositionX() != dist_x) or (frog.getCurrentPositionY() != dist_y):
    if frog.getCurrentPositionX() < dist_x:
        frog.moveRight()
    elif frog.getCurrentPositionX() > dist_x:
        frog.moveLeft()
    if frog.getCurrentPositionY() < dist_y:
        frog.moveUp()
    elif frog.getCurrentPositionY() > dist_y:
        frog.moveDown()
    frog.displayCurrentPosition()
# Input: current position of the frog, destination position of the frog
# Output: the path the frog takes to reach the destination position
    
