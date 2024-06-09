#include <stdio.h>
int main()
{
    long long int n, a = 0, sum1 = 0, sum2 = 0;
    scanf("%lld", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%lld", &a);
        sum1 += a;
    }
    for (int j = 0; j < n - 1; j++)
    {

        scanf("%lld", &a);
        sum2 += a;
    }
    printf("%lld", sum1 - sum2);

    return 0;
}