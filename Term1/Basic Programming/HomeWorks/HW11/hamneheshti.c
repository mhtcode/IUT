#include <stdio.h>
int main()
{
    int a, b, a1, b1, count = 2;
    scanf("%d%d", &a, &b);
    if (a >= b)
    {
        while (count <= a)
        {
            a1 = a % count;
            b1 = b % count;
            if (a1 == b1)
            {
                printf("%d ", count);
            }

            count += 1;
        }
    }

    else
    {
        while (count <= b)
        {
            a1 = a % count;
            b1 = b % count;
            if (a1 == b1)
            {
                printf("%d ", count);
            }

            count += 1;
        }
    }

    return 0;
}