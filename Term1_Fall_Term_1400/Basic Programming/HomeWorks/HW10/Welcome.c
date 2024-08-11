#include <stdio.h>
int main()
{
    float a, b, c, d, e, sum, sum1, avg, a1, b1, c1, d1, e1, variance;

    scanf("%f%f%f%f%f", &a, &b, &c, &d, &e);
    sum = a + b + c + d + e;
    avg = sum / 5;

    a1 = a - avg;
    a1 = a1 * a1;
    b1 = b - avg;
    b1 = b1 * b1;
    c1 = c - avg;
    c1 = c1 * c1;
    d1 = d - avg;
    d1 = d1 * d1;
    e1 = e - avg;
    e1 = e1 * e1;
    sum1 = a1 + b1 + c1 + d1 + e1;
    variance = sum1 / 5;

    printf("%.3f\n", sum);
    printf("%.3f\n", avg);
    printf("%.3f", variance);

    return 0;
}
