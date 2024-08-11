#include <iostream>

using namespace std;

struct Rational
{
    int a;
    int b;
};

int b_m_m(int a, int b)
{
    return b == 0 ? a : b_m_m(b, a % b);
}

void getRational(Rational *i)
{
    cout << "\aEnter value of a : ";
    cin >> i->a;

    cout << "\aEnter value of b : ";
    cin >> i->b;

    while (i->b == 0)
    {
        cout << "*** ERROR: The denominator cannot be zero. ***" << endl;
        cout << "please enter b (b != 0): ";
        cin >> i->b;
    }
    cout << endl;
}
void print(Rational i)
{
    cout << i.a << "/" << i.b << endl;
}
void simplify(Rational *i)
{
    int x = i->a;
    int y = i->b;

    int B;
    B = b_m_m(i->a, i->b);
    i->a /= B;
    i->b /= B;
}
Rational add(Rational q1, Rational q2)
{
    Rational q3;
    q3.a = (q1.a * q2.b) + (q2.a * q1.b);
    q3.b = (q1.b * q2.b);
    cout << "Total is : " << q3.a << "/" << q3.b << "    OR    ";
    simplify(&q3);
    cout << q3.a << "/" << q3.b << endl;
    cout << endl;
    return q3;
}
Rational subtract(Rational q1, Rational q2)
{
    Rational q3;
    q3.a = (q1.a * q2.b) - (q2.a * q1.b);
    q3.b = (q1.b * q2.b);
    cout << "Subtraction is : " << q3.a << "/" << q3.b << "    OR    ";
    simplify(&q3);
    if (q3.b < 0)
    {
        q3.a *= (-1);
        q3.b *= (-1);
    }
    cout << q3.a << "/" << q3.b << endl;
    cout << endl;

    return q3;
}
Rational multiply(Rational q1, Rational q2)
{
    Rational q3;
    q3.a = q1.a * q2.a;
    q3.b = q1.b * q2.b;
    cout << endl;
    return q3;
}
void reverse(Rational *i)
{
    int temp = i->b;
    i->b = i->a;
    i->a = temp;
    cout << "Reverse is : " << i->a << "/" << i->b << endl;
    cout << endl;
}

Rational divide(Rational q1, Rational q2)
{
    Rational Div;
    Div.a = q1.a * q2.b;
    Div.b = q2.b * q2.a;
    simplify(&Div);
    cout << "Divide is : " << Div.a << "/" << Div.b << endl;
    cout << endl;
    return Div;
}

int main()
{
    Rational q1, q2, q3, q4, q5;
    getRational(&q1);
    getRational(&q2);
    cout << endl;
    cout << "q1 is : ";
    print(q1);
    cout << "q2 is : ";
    print(q2);
    cout << endl;
    simplify(&q1);
    q3 = add(q1, q2);
    q4 = subtract(q1, q2);
    q5 = multiply(q1, q2);
    reverse(&q5);
    divide(q1, q2);
    return 0;
}
