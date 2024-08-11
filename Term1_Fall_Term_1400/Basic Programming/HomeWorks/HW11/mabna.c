#include <stdio.h>
int main()
{
    int a, b, sum1 = 0, sum2 = 0, baghimande = 0, count = 1, javab = 0;
    scanf("%d%d", &a, &b);
    while (a > 0)
    {
        baghimande = a % b;
        if ((count - 1) % 2 == 0)
        {
            sum1 += baghimande;
        }
        else
        {
            sum2 += baghimande;
        }
        count++;
        a /= b;
        if ((sum1 == sum2) && a == 0)
        {
            javab = 1;
            break;
        }
    }
    if (javab == 1)
        printf("Yes");
    else
        printf("No");

    return 0;
}