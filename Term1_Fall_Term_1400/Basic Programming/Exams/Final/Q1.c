#include <stdio.h>
int main()
{
    int array1[1000];
    int adad = 0;
    int index = 0;
    int adad2 = 0;
    int temp = 1;
    while (temp != 0)
    {
        scanf("%d", &adad);
        if (adad == 1)
        {
            scanf("%d", &adad2);
            array1[index] = adad2;
            index++;
        }
        else if (adad == 2)
        {
            if (index == 0)
                printf("stack is empty\n");
            else
            {
                printf("%d\n", array1[index - 1]);
                index--;
            }
        }
        else if (adad == 3)
        {
            if (index == 0)
                printf("stack is empty\n");
            else
                printf("%d\n", array1[index - 1]);
        }
        else if (adad == 4)
            temp = 0;
    }

    return 0;
}
