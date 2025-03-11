#include <iostream>

class Foo
{
};

int main()
{
    Foo *obj = new Foo();
    Foo *obj2 = new Foo();
    Foo *obj3 = new Foo();

    delete obj;
    delete obj2;
    delete obj3;
    return 0;
}