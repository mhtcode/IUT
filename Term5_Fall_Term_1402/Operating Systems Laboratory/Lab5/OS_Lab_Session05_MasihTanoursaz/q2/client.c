#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <unistd.h>
#include <math.h>

#define FIFO_PATH "./q2.pipe"

typedef struct Data
{
    char opperator;
    int opperand1, opperand2;
} myData;

int main()
{
    long ans;
    while (1)
    {
        myData data;
        printf("Enter opperator:\n");
        scanf("%c", &data.opperator);
        printf("Enter first opperand:\n");
        scanf("%d", &data.opperand1);
        printf("Enter second opperand:\n");
        scanf("%d", &data.opperand2);
        getchar();
        int fd = open(FIFO_PATH, O_WRONLY);
        write(fd, &data, sizeof(struct Data));
        close(fd);
        fd = open(FIFO_PATH, O_RDONLY);
        read(fd, &ans, sizeof(ans));
        printf("Answer is %ld\n", ans);
        close(fd);
    }

    return 0;
}
