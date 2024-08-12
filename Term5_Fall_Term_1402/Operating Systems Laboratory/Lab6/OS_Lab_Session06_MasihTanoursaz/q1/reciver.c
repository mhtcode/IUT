#include "protocol.h"
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>

int main()
{
    int fd = shm_open(NAME, O_RDONLY, 0666);
    if (fd < 0)
    {
        perror("shm_open()");
        return EXIT_FAILURE;
    }

    int size = 2 * sizeof(struct myData);

    struct myData *data;
    data = (struct myData *)mmap(0, size, PROT_READ,
                                 MAP_SHARED, fd, 0); // mmap(): Permission denied

    if (data == (struct myData *)-1)
    {
        perror("mmap()");
        return EXIT_FAILURE;
    }

    printf("reciver address: %p\n", data);

    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < NUM; j++)
        {
            printf("Number %d in %d is %d \n\n", j, i, data[i].intArr[j]);
        }
        printf("Message %d is %s \n\n", i, data[i].strArr);
    }

    munmap(data, size);

    close(fd);

    // delete file
    shm_unlink(NAME);
    return EXIT_SUCCESS;
}