#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>
#include <string.h>
#include "protocol.h"
#include <time.h>

int main()
{
    int fd = shm_open(NAME, O_CREAT | O_EXCL | O_RDWR, 0600);
    if (fd < 0)
    {
        perror("shm_open()");
        return EXIT_FAILURE;
    }

    int size = 2 * sizeof(struct myData);

    ftruncate(fd, size);

    struct myData *data;
    data = (struct myData *)mmap(0, size, PROT_WRITE,
                                 MAP_SHARED, fd, 0);
    if (data == (struct myData *)-1)
    {
        perror("mmap()");
        return EXIT_FAILURE;
    }

    printf("sender address: %p\n", data);
    srand(time(NULL));

    for (int i = 0; i < NUM; i++)
    {
        data[0].intArr[i] = rand() % 5 + 1;
        data[1].intArr[i] = rand() % 5 + 1;
    }

    strncpy(data[0].strArr, "Masih", STR_L);
    strncpy(data[1].strArr, "Ardalan", STR_L);

    munmap(data, size);

    close(fd);
    return EXIT_SUCCESS;
}