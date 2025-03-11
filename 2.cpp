#include <iostream>
#include <cmath>

using namespace std;

class Point
{
private:
    double X, Y;

public:
    Point()
    {
        // this is a constructor;
    }
    Point(double x, double y) : X(x), Y(y) {};
    ~Point()
    {
        // this is a destructor;
    }
    void setX(double x) { X = x; }
    void setY(double y) { Y = y; }
    void setCoor(double x, double y)
    {
        X = x;
        Y = y;
    }
    double getX() { return X; }
    double getY() { return Y; }
    void print()
    {
        std::cout << "(" << X << ", " << Y << ")";
    }
};

class Segment
{
private:
    Point start, end;

public:
    Segment() {}
    Segment(Point s, Point e) : start(s), end(e) {}
    void setStart(Point s) { start = s; }
    void setEnd(Point e) { end = e; }
    double distance()
    {
        double x = pow(end.getX() - start.getX(), 2);
        double y = pow(end.getY() - start.getY(), 2);
        return sqrt(x + y);
    }
};
int main()
{
    Segment seg;
    Point temp;
    int numOfSegments = 0;
    double x = 0, y = 0, x1 = 0, y1 = 0;
    std::cin >> numOfSegments;
    while (numOfSegments--)
    {
        std::cin >> x >> y >> x1 >> y1;
        temp.setX(x);
        temp.setY(y);
        seg.setStart(temp);
        temp.setX(x1);
        temp.setY(y1);
        seg.setEnd(temp);
        std::cout << seg.distance() << std::endl;
    }
    return 0;
}