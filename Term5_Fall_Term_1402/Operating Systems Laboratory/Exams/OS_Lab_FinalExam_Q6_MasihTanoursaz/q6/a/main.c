#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>

int *bag, max = 100, use = 0, fill = 0, done = 0;
sem_t empty, full, mutex;
void do_fill(int value)
{
    bag[fill] = value;
    fill++;
    if (fill == max)
        fill = 0;
}
int do_get()
{
    int tmp = bag[use];
    use++;
    if (use == max)
        use = 0;
    return tmp;
}

void *boss(void *arg)
{
    int i = 0;
    while (1)
    {
        srand(time(NULL));
        /* block A:*/
        i = (rand() % 10) + 1;
        sem_wait(&mutex);
        sem_wait(&empty);
        if (done != 1) // (fill != max) can make some bugs in espetial situations
            do_fill(i);
        sem_post(&empty);
        sem_post(&mutex);

        if (done == 1)
        {
            printf("Game is done (Boss)\n");
            return (NULL);
        }
    }
}
void *player(void *arg)
{
    int sum = 0;
    while (1)
    {
        /* block B:*/
        sem_wait(&full);
        sem_wait(&mutex);
        if (done == 1)
            printf("Game is done\n");
        else
        {
            sum = sum + do_get();
            if (sum > 100)
            {
                done = 1;
                printf("I am the winner (player: %lld)\n",
                       (long long int)arg);
            }
            /* block C:*/
            sem_post(&mutex);
            sem_post(&full);

            printf("%lld %d\n", (long long int)arg, sum);
            if (done == 1)
            {
                printf("Game is done (player: %lld)\n", (long long int)arg);
                return (NULL);
            }
        }
    }
}

int main(int arg, char *argv[])
{
    bag = (int *)malloc(max * sizeof(int));
    srand(time(NULL));
    int i;
    /* block D:*/
    sem_init(&empty, 0, 1);
    sem_init(&full, 0, 5);
    sem_init(&mutex, 0, 1);

    pthread_t bid, pid[5];
    pthread_create(&bid, NULL, boss, NULL);
    for (i = 0; i < 5; i++)
    {
        pthread_create(&pid[i], NULL, player, (void *)(long long int)i);
    }
    pthread_join(bid, NULL);
    for (i = 0; i < 5; i++)
    {
        pthread_join(pid[i], NULL);
    }

    return 0;
}
