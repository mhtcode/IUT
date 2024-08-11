#include <stdio.h>
int main()
{
    int x, y, n, r1, k, q1, r2;

    scanf("%d%d%d", &x, &y, &n);
    r1 = n - x;
    r2 = r1 % y;
    q1 = (r1 - r2) / y;

    k = (y * q1) + x;
    printf("%d", k);

    return 0;
}
