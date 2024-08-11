#include <stdio.h>

int main()
{
    int N, dig[100], i, j, s, t, k, l, temp;

    scanf("%d", &N);

    for (;;)
    {
        for (i = j = 100; N > 0;)
        {
            dig[--i] = N % 10;
            N = N / 10;
        }
        for (s = j - 2; s >= i; s--)
        {
            if (dig[s] < dig[s + 1])
            {
                break;
            }
        }
        if (s < i)
        {
            printf("%d", 0);
            break;
        }
        t = s + 1;
        for (k = t + 1; k < j; k++)
        {
            if (dig[k] < dig[t] && dig[k] > dig[s])
            {
                t = k;
            }
        }
        temp = dig[t];
        dig[t] = dig[s];
        dig[s] = temp;
        for (k = s + 1; k < j; k++)
        {
            for (l = k + 1; l < j; l++)
            {
                if (dig[k] > dig[l])
                {
                    temp = dig[k];
                    dig[k] = dig[l];
                    dig[l] = temp;
                }
            }
        }
        N = 0;
        for (k = i; k < j; k++)
        {
            N = N * 10 + dig[k];
            printf("%d", dig[k]);
        }
        break;
    }
    return 0;
}