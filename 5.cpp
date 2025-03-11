#include <iostream>

class Frog
{
private:
    int x, y;

public:
    Frog(int x, int y) : x(x), y(y) {}
    void moveLeft() { x--; }
    void moveRight() { x++; }
    void moveUp() { y++; }
    void moveDown() { y--; }
    int getCurrentPositionX() { return x; }
    int getCurrentPositionY() { return y; }
    void print()
    {
        std::cout << x << " " << y << std::endl;
    }
};

int main()
{
    int x, y, finalX, finalY;
    std::cin >> x >> y;
    Frog frog(x, y);
    std::cin >> finalX >> finalY;
    while ((frog.getCurrentPositionX() != finalX) || (frog.getCurrentPositionY() != finalY))
    {
        if (frog.getCurrentPositionX() < finalX)
            frog.moveRight();
        else if (frog.getCurrentPositionX() > finalX)
            frog.moveLeft();
        if (frog.getCurrentPositionY() < finalY)
            frog.moveUp();
        else if (frog.getCurrentPositionY() > finalY)
            frog.moveDown();
    }
    frog.print();

    return 0;
}