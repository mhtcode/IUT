#include <stdio.h>
int havedigits_N_M(int N, int M, int number);
int main()
{
    long int number;
    scanf("%d", &number);
    printf("%d", havedigits_N_M(0, 1, number));

    return 0;
}

int havedigits_N_M(int N, int M, int number)
{
    int reminder = 0, count = 0;
    int i = 1;
    int j;
    while (i <= number)
    {
        j = i;
        while (j != 0)
        {
            reminder = j % 10;
            if (reminder == N || reminder == M)
            {
                j -= reminder;
                j /= 10;
            }
            else
                break;
            if (j == 0)
                count += 1;
        };
        i++;
    }
    return count;
}
