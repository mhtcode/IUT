#!/bin/bash
MAJOR=240
MINOR=0

make
sudo insmod driver.ko
sudo mknod /dev/game c  "0x$MAJOR" "0x$MINOR"
gcc main.c -o main
sudo ./main
sudo rmmod driver
sudo rm -f /dev/game
rm main
make clean