#include <stdio.h>
#include <math.h>
double fact(int n)
{
    if (n == 1)
        return 1;

    return n * fact(n - 1);
}

double sum(int x, int n)
{
    double i, total = 0;

    for (i = 0; i < n; i++)
    {
        if (i == 0)
        {
            total = 1;
            continue;
        }
        total += (pow(x, i) / fact(i));
    }
    return total;
}

int main()
{

    int x, n;
    scanf("%d", &x);
    scanf("%d", &n);

    printf("%.3f", sum(x, n));

    return 0;
}