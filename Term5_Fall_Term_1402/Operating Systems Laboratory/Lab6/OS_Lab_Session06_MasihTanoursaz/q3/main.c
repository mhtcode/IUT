#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <signal.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <sys/wait.h>

#define ARRAY_SIZE 20
#define MAX_CHILD 5

int act_by_sig1 = 0;
int act_by_sig2 = 0;

void handler(int signo)
{
    printf("SIGNAL recieved in child\n");
    switch (signo)
    {
    case SIGUSR1:
        act_by_sig1 = 1;
        break;
    case SIGUSR2:
        act_by_sig2 = 1;
        break;
    }
}

void task(int id, int *data)
{
    printf("child %d is running task.\n", id);
    pause();

    printf("child %d activated by signal %d\n", id, (act_by_sig2) ? 2 : 1);
    if (act_by_sig1 || act_by_sig2)
    {
        for (int i = id; i < ARRAY_SIZE; i += MAX_CHILD)
        {
            if (act_by_sig1)
                data[i] = 3 * data[i] + 3;
            else
                data[i] = 2 * data[i] + 1;
        }
    }
    printf("child %d done\n", id);
    exit(0);
}

int main()
{
    struct sigaction action1;
    action1.sa_handler = handler;
    action1.sa_flags = 0;
    sigemptyset(&action1.sa_mask);

    sigaction(SIGUSR1, &action1, NULL);
    sigaction(SIGUSR2, &action1, NULL);
    int size = ARRAY_SIZE * sizeof(int);
    int *data = (int *)mmap(0, size, PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, 0, 0);
    if (data == (void *)-1)
    {
        perror("mmap()");
        return EXIT_FAILURE;
    }
    pid_t childs[MAX_CHILD];
    for (int i = 0; i < MAX_CHILD; i++)
    {
        childs[i] = fork();
        if (childs[i] == -1)
            return EXIT_FAILURE;
        else if (childs[i] == 0)
        {
            task(i, data);
        }
    }
    usleep(100000);
    for (int i = 0; i < ARRAY_SIZE; i++)
    {
        data[i] = i;
    }

    for (int i = 0; i < MAX_CHILD; i++)
    {
        if (i % 2 == 1)
            kill(childs[i], SIGUSR1);
        else
            kill(childs[i], SIGUSR2);

        usleep(100);
    }
    int status;
    for (int i = 0; i < MAX_CHILD; i++)
    {
        printf("in parent, waiting for childs\n");
        if (waitpid(childs[i], &status, 0) == -1)
            perror("can not wait!\n");
        else
            printf("child %d terminated.\n", i);
    }

    for (int i = 0; i < ARRAY_SIZE; i++)
    {
        if (i % 10 == 0)
            printf("\n");
        printf("%d\t", data[i]);
    }
    printf("\n");
    munmap(data, size);
    return 0;
}
