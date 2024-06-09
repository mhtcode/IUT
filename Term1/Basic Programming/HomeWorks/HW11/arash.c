#include <stdio.h>

int main()
{
    int n, adad, b, c, javab, sum1, sum2;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {

        scanf("%d", &adad);
        if (adad > 300)
        {
            b = adad - 300;
            javab = 0;
            c = b;
            for (int j = 0; j < 300; j++)
            {
                b = c;
                sum1 = 0;
                sum2 = 0;
                while (b != 0)
                {
                    sum1 += b % 10;
                    b /= 10;
                }
                sum2 += sum1 + (c);
                c++;
                if (sum2 == adad)
                {
                    javab = 1;
                }
            }
            if (javab == 0)
                printf("No\n");
            else
                printf("Yes\n");
        }
        else
        {
            b = 1;
            javab = 0;
            c = b;
            for (int j = 0; j < 300; j++)
            {
                b = c;
                sum1 = 0;
                sum2 = 0;
                while (b != 0)
                {
                    sum1 += b % 10;
                    b /= 10;
                }
                sum2 += sum1 + (c);
                c++;
                if (sum2 == adad)
                {
                    javab = 1;
                    break;
                }
                if (c == adad)
                    break;
            }
            if (javab == 0)
                printf("No\n");
            else
                printf("Yes\n");
        }
    }

    return 0;
}
