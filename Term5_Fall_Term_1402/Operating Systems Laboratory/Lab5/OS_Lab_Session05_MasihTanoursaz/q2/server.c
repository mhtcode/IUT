#include <stdio.h>
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
    mkfifo(FIFO_PATH, 0777);
    long ans;
    while (1)
    {
        while (1)
        {
            int fd = open(FIFO_PATH, O_RDONLY);
            myData data;
            if (read(fd, &data, sizeof(struct Data)) > 0)
            {
                if (data.opperator == 'm')
                {
                    ans = data.opperand1 * data.opperand2;
                    printf("in server %d * %d = %ld\n", data.opperand1, data.opperand2, ans);
                }
                else if (data.opperator == 'p')
                {
                    ans = pow(data.opperand1, data.opperand2);
                    printf("in server %d ** %d = %ld\n", data.opperand1, data.opperand2, ans);
                }
            }
            close(fd);
            break;
        }
        int fd = open(FIFO_PATH, O_WRONLY);
        write(fd, &ans, sizeof(ans));
        close(fd);
    }
    return 0;
}
