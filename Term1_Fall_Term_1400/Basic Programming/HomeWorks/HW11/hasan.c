#include <stdio.h>
int main()
{
    int x, y, n, x1, y1, n1;
    scanf("%d%d%d", &n, &x, &y);
    n1 = n;

    if (n % x == 0)
    {
        x1 = n / x;
        printf("%d %d", x1, 0);
    }
    else if (n % y == 0)
    {
        y1 = n / y;
        printf("%d %d", 0, y1);
    }
    else
    {
        x1 = 0;
        y1 = 0;
        while (n - x > 0)
        {
            n -= x;
            x1++;
            if (n % y == 0)
            {
                y1 = n / y;
                break;
            }
        }
        if (x1 * x + y1 * y == n1)
            printf("%d %d", x1, y1);
        else
            printf("%d", -1);
    }

    return 0;
}