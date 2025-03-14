#include <iostream>

using namespace std;

class Point
{
public:
    double X, Y;
    Point()
    {
        // this is a constructor;
    }
    Point(double x, double y)
    {
        X = x;
        Y = y;
    }
    ~Point()
    {
        // this is a destructor;
    }
    void print()
    {
        std::cout << "(" << X << ", " << Y << ")";
    }
};
int main()
{
    Point data;
    int iter = 0;
    double x = 0, y = 0;
    std::cin >> iter;
    while (iter--)
    {
        std::cin >> x >> y;
        data.X = x;
        data.Y = y;
        data.print();
        std::cout << endl;
    }
    return 0;
}