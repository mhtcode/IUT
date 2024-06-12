
#include <sys/ioctl.h>
#include <fcntl.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "utills.h"
#include <stdio.h>
int main(int argc, char **argv)
{
    int fd, retp;
    char read_data[64];
    struct iut_data *mywallet = malloc(sizeof(struct iut_data));
    memset(mywallet, 0, sizeof(struct iut_data));
    fd = open("/dev/myWallet", O_RDWR);
    if (fd < 0)
    {
        perror("open");
        exit(0);
    }

    // TEST 1 -->> change status and get status
    // ioctl(fd, getStatus, mywallet);
    // retp = ioctl(fd, changeStatus, mywallet);
    // ioctl(fd, getStatus, mywallet);
    // retp = ioctl(fd, changeStatus, mywallet);
    // ioctl(fd, getStatus, mywallet);
    //---------------------------------------------------------------
    // TEST 2 -->> read(ERROR is locked should print in kernel)
    // read(fd, read_data, 64);
    // printf("Data in wallat is: %s\n", read_data);
    //---------------------------------------------------------------
    // TEST 3 -->> read(works truly)
    // strcpy(mywallet->password, "1234");
    // ioctl(fd, changeStatus, mywallet);
    // read(fd, read_data, 64);
    // printf("Data in wallat is: %s\n", read_data);
    //---------------------------------------------------------------
    // TEST 4 -->> change password
    // strcpy(mywallet->password, "1234");
    // strcpy(mywallet->new_password, "4321");
    // ioctl(fd, changePass, mywallet);
    //---------------------------------------------------------------
    // TEST 5 -->> write and get content
    // struct iut_data *mywallet1 = malloc(sizeof(struct iut_data));
    // memset(mywallet1, 0, sizeof(struct iut_data));
    // char mySecret[64] = "Ajaaab AZI:/";
    // strcpy(mywallet1->password, "1234");
    // ioctl(fd, changeStatus, mywallet);
    // write(fd, mySecret, strlen(mySecret));
    // ioctl(fd, getContent, mywallet);
    // printf("Data in wallat is: %s\n", mywallet->message);

    close(fd);

    return 0;
}
