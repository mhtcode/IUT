#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/time.h>
#include <time.h>
#include <signal.h>

#define MAXCHILD 5
#define MAXNUM 100

void task(int id, int fd[2])
{
    while (1)
    {
        srand(time(NULL) + id * id);
        int time_sleep = rand() % 5 + 1;
        printf("for child %d random number is %d\n", getpid(), time_sleep);
        write(fd[1], &time_sleep, sizeof(time_sleep));
        sleep(time_sleep);
    }
}

int main()
{
    int TOTAL = 0;
    pid_t childsArr[MAXCHILD];
    int fd[2];
    int data;
    int x = pipe(fd);
    if (!x)
    {
        for (int i = 0; i < MAXCHILD; i++)
        {
            pid_t child = fork();
            if (child == 0)
            {
                // in child
                close(fd[0]);
                task(i, fd);
                break;
            }
        }
        while (1)
        {
            close(fd[1]);
            if (read(fd[0], &data, sizeof(data)) > 0)
            {
                TOTAL += data;
                printf("Data is: %d,TOTAL is: %d \n", data, TOTAL);
                if (TOTAL >= MAXNUM)
                {
                    kill(0, SIGKILL);
                    exit(0);
                }
            }
            else
                printf("pipe is not available\n");
        }
    }
    else
    {
        printf("Pipe is not accessable %d.\n", x);
        exit(0);
    }

    return 0;
}
