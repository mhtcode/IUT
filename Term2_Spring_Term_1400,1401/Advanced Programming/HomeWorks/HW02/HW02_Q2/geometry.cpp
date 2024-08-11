#include <iostream>
#include "geometry.h"
#include <math.h>

using namespace std;

void point::setX(int tool)
{
    x = tool;
}
void point::setY(int arz)
{
    y = arz;
}
void point::setAll(int tool, int arz)
{
    x = tool;
    y = arz;
}

int point::getX()
{
    return x;
}
int point::getY()
{
    return y;
}
int point::lengh()
{
    return sqrt(x * x + y * y);
}

void point::showPoint()
{
    cout << '(' << x << ',' << y << ')' << endl;
}

int main()
{
    point p1;
    p1.setX(3);
    p1.setY(4);
    cout << p1.getX() << endl;
    cout << p1.getY() << endl;
    cout << p1.lengh() << endl;
    p1.showPoint();
    point p2(8, 10);
    p2.showPoint();
    point p3;
    p3.showPoint();

    return 0;
}