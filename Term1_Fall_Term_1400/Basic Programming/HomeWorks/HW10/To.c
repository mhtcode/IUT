#include <stdio.h>
int main()
{
    int a, b, ekhtelaf, r, q, x;

    scanf("%d%d", &a, &b);
    ekhtelaf = a - b;
    r = ekhtelaf % 10;
    x = ((r) != 0);
    q = (ekhtelaf - r) / 10;

    printf("%d", q + x);
    return 0;
}
