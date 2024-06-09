#include <stdio.h>
#include <stdlib.h>

void ShowFibNth(long int n, long int nplus);

int main()
{
    int n, nplus;
    scanf("%ld%ld", &n, &nplus);
    ShowFibNth(n, nplus);

    return 0;
}

void ShowFibNth(long int n, long int nplus)
{
    int shomaresh = 0;
    if (shomaresh == 0)
    {
        printf("%d\n", n);
        shomaresh++;
        nplus = nplus - n;
        if (nplus == 0)
            exit(0);
    }

    if (shomaresh == 1)
    {
        printf("%d\n", nplus);
        shomaresh++;
        n = n - nplus;
        if (n == 0)
            exit(0);
    }

    ShowFibNth(n, nplus);
}
