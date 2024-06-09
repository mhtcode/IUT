#include <stdio.h>

void PrintArray(int *a, int N);
void ArraySort(int *a, int N);
void Swap(int *p1, int *p2);

int main()
{
    int index;
    scanf("%d", &index);
    int a[index];
    for (int i = 0; i < index; i++)
    {
        int adad;
        scanf("%d", &adad);
        a[i] = adad;
    }

    ArraySort(a, index);

    printf("Array after sorting -> ");
    PrintArray(a, index);
    printf("\n");

    return 0;
}

void ArraySort(int *a, int N)
{
    int i, j;
    int swapped;

    for (i = 0; i < N; i++)
    {
        swapped = 0;
        for (j = 0; j < N - 1; j++)
        {
            if (a[j] > a[j + 1])
            {
                Swap(&a[j], &a[j + 1]);
                swapped = 1;
            }
        }
        if (!swapped)
            break;
    }
}

void Swap(int *p1, int *p2)
{
    int temp;
    temp = *p1;
    *p1 = *p2;
    *p2 = temp;
}

void PrintArray(int *a, int N)
{
    int i;
    for (i = 0; i < N; i++)
    {
        printf("%d", a[i]);
        if (i < N - 1)
        {
            printf(", ");
        }
    }
}
