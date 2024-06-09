#include <stdio.h>
int main()
{
    int n, x1, y1, x2, y2, x3, y3;
    float shib = 0, arz = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d%d%d%d%d%d", &x1, &y1, &x2, &y2, &x3, &y3);

        if (x1 == x2 && y1 == y2)
        {
            printf("not a triangle\n");
            continue;
        }
        else if (x1 == x3 && y1 == y3)
        {
            printf("not a triangle\n");
            continue;
        }
        else if (x2 == x3 && y2 == y3)
        {
            printf("not a triangle\n");
            continue;
        }
        else if (x1 == x2 && x2 == x3)
        {
            printf("not a triangle\n");
            continue;
        }
        if (x2 - x1 != 0)
        {

            shib = (y2 - y1) / (x2 - x1);
            arz = y1 - shib * x1;
            if (y3 == shib * x3 + arz)
            {
                printf("not a triangle\n");
                continue;
            }
        }
        if (x3 - x1 != 0)
        {

            shib = (y3 - y1) / (x3 - x1);
            arz = y1 - shib * x1;
            if (y2 == shib * x2 + arz)
            {
                printf("not a triangle\n");
                continue;
            }
        }
        if (1)
        {
            int a, b, c, cos_a, cos_b, cos_c;

            a = (y2 - y1) * (y2 - y1) + (x2 - x1) * (x2 - x1);
            b = (y3 - y1) * (y3 - y1) + (x3 - x1) * (x3 - x1);
            c = (y3 - y2) * (y3 - y2) + (x3 - x2) * (x3 - x2);
            cos_a = (b + c - a);
            cos_b = (a + c - b);
            cos_c = (b + a - c);

            if (a == b || a == c || b == c) // isosceles
            {
                if (a == b + c || b == a + c || c == a + b) // right
                {
                    printf("isosceles right triangle\n");
                    continue;
                }
                else if (cos_a > 0 && cos_b > 0 && cos_c > 0) // acute
                {
                    printf("isosceles acute triangle\n");
                    continue;
                }
                else
                {
                    printf("isosceles obtuse triangle\n");
                    continue;
                }
            }
            else
            {
                if (a == b + c || b == a + c || c == a + b) // right
                {
                    printf("scalene right triangle\n");
                    continue;
                }
                else if (cos_a > 0 && cos_b > 0 && cos_c > 0) // acute
                {
                    printf("scalene acute triangle\n");
                    continue;
                }
                else
                {
                    printf("scalene obtuse triangle\n");
                    continue;
                }
            }
        }

        return 0;
    }
}