#include <stdio.h>
#include <math.h>

int main()
{
    int N;

    scanf("%d", &N);

    int a, b, temp = 1;
    for (a = 0; a < N; a++)
    {
        for (b = 0; b < N; b++)
        {
            if (temp == 0)
                break;
            if ((a < b) && (b < N - a - b))
            {
                if (pow(a, 2) + pow(b, 2) == pow(N - a - b, 2))
                {
                    printf("%d %d %d", a, b, N - a - b);
                    temp = 0;
                    break;
                }
            }
        }
    }
    if (temp == 1)
        printf("Impossible");
}
