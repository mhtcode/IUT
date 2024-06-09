#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);
    int p, q, k = 0, temp;
    int lst[2 * n];
    int count = 0;
    for (int i = 0; i < n; i++)
    {
        scanf("%d%d", &p, &q);
        lst[k] = p;
        lst[k + 1] = q;
        k += 2;
    }
    int i = 0;
    while (i < n * 2)
    {
        int j = 0;
        while (j < n * 2)
        {
            if (i == j)
                j += 2;
            if (lst[i] >= lst[j])
            {
                if (lst[i + 1] <= lst[j + 1])
                {
                    count += 1;
                    break;
                }
            }
            if (j == (n - 1) * 2)
                break;
            j += 2;
        }
        i += 2;
    }
    printf("%d", n - count);

    return 0;
}