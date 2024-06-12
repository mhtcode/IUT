#include <sys/ioctl.h>
#include <fcntl.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <semaphore.h>
#include <sys/stat.h>
#include <sys/mman.h>
#include "utills.h"

// defines for semaphores and device name
#define SEM_MUTEX "/mu"
#define SEM_FULL "/fu"
#define SEM_EMPTY "/em"
#define SHM_NAME "/sh"
#define SEM_PERMS (S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP)
#define DEVICE_NAME "/dev/game"

// typdef structs of utils.h
typedef struct iut_data *struct_iut;
typedef struct shm_struct *struct_sharemem;

void close_all(sem_t *mutex, sem_t *full, sem_t *empty)
{
    sem_close(mutex);
    sem_close(full);
    sem_close(empty);
}

void player(struct_iut d, int fd, int id, struct_sharemem doneStatus)
{
    int sum = 0;
    sem_t *mutex = sem_open(SEM_MUTEX, O_RDWR);
    sem_t *full = sem_open(SEM_FULL, O_RDWR);
    sem_t *empty = sem_open(SEM_EMPTY, O_RDWR);
    while (1)
    {
        if (doneStatus->done == 1) // game has been finished,all other process should be killed
        {
            exit(0);
        }
        if (sum >= 100) // the winner, sum is more than 100
        {
            printf("I am the winner (player: %d)\n", id);
            close_all(mutex, full, empty); // close all semaphores
            doneStatus->done = 1;          // game has been finished
            exit(0);
        }
        sem_wait(full);
        sem_wait(mutex);
        ioctl(fd, do_get, d);
        sum = d->sum;
        printf("playe id %d, sum: %d, done: %d\n", id, sum, doneStatus->done);
        sem_post(mutex);
        sem_post(full);
    }
}

void boss(struct_iut d, int fd, struct_sharemem doneStatus)
{
    sem_t *mutex = sem_open(SEM_MUTEX, O_RDWR);
    sem_t *full = sem_open(SEM_FULL, O_RDWR);
    sem_t *empty = sem_open(SEM_EMPTY, O_RDWR);
    while (1)
    {
        sem_wait(mutex);
        sem_wait(empty);
        ioctl(fd, do_fill, d);
        sem_post(empty);
        sem_post(mutex);
        if (doneStatus->done == 1) // game has been finished
        {
            close_all(mutex, full, empty);
            exit(0);
        }
    }
}

int main()
{
    // initialize variables
    int fd, ret, retp;
    struct shm_struct *doneStatus;
    pid_t p;
    sem_t *mutex, *full, *empty;
    // initialize semaphores
    empty = sem_open(SEM_EMPTY, O_CREAT | O_EXCL, SEM_PERMS, 1);
    full = sem_open(SEM_FULL, O_CREAT | O_EXCL, SEM_PERMS, 5);
    mutex = sem_open(SEM_MUTEX, O_CREAT | O_EXCL, SEM_PERMS, 1);

    close_all(mutex, full, empty);

    struct_iut iut_data1 = malloc(sizeof(struct iut_data));
    memset(iut_data1, -1, sizeof(struct iut_data));

    fd = open(DEVICE_NAME, O_RDWR);

    // Shared Memory Open For Store Global Variable 'Done'
    int shm_fd = shm_open(SHM_NAME, O_CREAT | O_EXCL | O_RDWR, 0600);
    ftruncate(shm_fd, sizeof(struct shm_struct));
    void *data = mmap(0, sizeof(struct shm_struct), PROT_READ | PROT_WRITE, MAP_SHARED, shm_fd, 0);
    doneStatus = (struct_sharemem)data;
    doneStatus->done = 0;

    // Validation of Creating file descriptors
    if (fd < 0)
    {
        perror("open");
        exit(0);
    }

    // Run Processes
    iut_data1->sum = 0;
    for (int i = 0; i < 5; i++)
    {
        p = fork();
        if (p == 0)
            player(iut_data1, fd, i, doneStatus);
        else
        {
            boss(iut_data1, fd, doneStatus);
        }
    }
    // all players should killed and then program finishes
    for (int i = 0; i < 5; i++)
        wait(NULL);
    sem_unlink(SEM_MUTEX);
    sem_unlink(SEM_FULL);
    sem_unlink(SEM_EMPTY);
    shm_unlink(SHM_NAME);
    munmap(data, sizeof(struct shm_struct));
    close(shm_fd);
    close(fd);

    return 0;
}
