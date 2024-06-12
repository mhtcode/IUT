#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/time.h>
#include <time.h>

#define MAXCHILD 10

void cpusleep(int timesleep)
{
    int start = time(NULL);
    while(1)
    {
        int end = time(NULL);
        if(difftime(end, start)>= timesleep)
        return;
    }
}


void task(int id)
{
    srand(time(NULL) + id * id);
    int time_sleep =  rand() % 5 + 1;
    // sleep(time_sleep);
    cpusleep(time_sleep);
    printf("Task %d has been done by child %d in %d seconds.\n", id, getpid(), time_sleep);
    exit(0);
}


int main(int argc, char *argv[])
{
    pid_t childsArr[MAXCHILD];
    for(int i=0; i<=MAXCHILD; i++)
    {
        pid_t child = fork();
        if(child == 0)
        {
            // in child
            task(i);
        }
        else if(child > 0)
        {
            childsArr[i] = child;
        }

    }

    while(1)
    {
        sleep(5);
        for(int j=0; j<MAXCHILD; j++)
        {
            int status = waitpid(childsArr[j], NULL, WNOHANG);
            if (!status) continue;
            pid_t newChild = fork();
            if (newChild ==0)
            {
                task(j);
            }
            else if( newChild > 0)
            {
                childsArr[j] = newChild;
            }
        }
    }
    return 0;
}
