#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/fs.h>
#include <linux/miscdevice.h>
#include <linux/module.h>
#include <linux/netdevice.h>
#include <linux/list.h>
#include <linux/version.h>
#include <linux/wait.h>
#include <asm/uaccess.h>
#include "utills.h"
#include <linux/semaphore.h>
#include <linux/random.h>
#define DEVICE_NAME "game"

MODULE_LICENSE("GPL");
// initialize global variables
int bag[100];
int max = 100;
static int use = 0, fill = 0;
static int major;

void do_fill_func(struct iut_data *data)
{
    int i;
    get_random_bytes(&i, sizeof(i));
    if (i < 0) // because of generate random bytes, it would be negative my be,  and should chnge it to postive
        i *= -1;
    i = (i % 10) + 1; // between 1 to 10
    printk("in do_fill %d\n", i);
    bag[fill] = i;
    fill++;
    if (fill == max)
        fill = 0;
}

void do_get_func(struct iut_data *data)
{
    int temp = bag[use];
    int old_sum = data->sum;
    int new_sum = old_sum + temp;
    use++;
    printk("in do_get %d\n", temp);
    if (use == max)
        use = 0;
    data->sum = new_sum;
}

static long iut_ioctl(struct file *file, unsigned int req, unsigned long pointer)
{
    struct iut_data *data;
    int output;
    data = kzalloc(sizeof(struct iut_data), GFP_KERNEL);
    if (!data)
        return -ENOMEM;
    if (copy_from_user(data, (void *)pointer, sizeof(struct iut_data)))
        return -EFAULT;
    switch (req)
    {
    case do_fill:
        do_fill_func(data);
        break;

    case do_get:
        do_get_func(data);
        break;
    }

    output = copy_to_user((void *)pointer, data, sizeof(struct iut_data));

    return 1;
}

static int iut_open(struct inode *inode, struct file *file)
{
    printk("device opened\n");
    for (int i = 0; i < 100; i++)
        bag[i] = -1;
    use = 0;
    fill = 0;
    return 0;
}
static int iut_release(struct inode *inode, struct file *file)
{
    printk("device closed\n");
    return 0;
}

static const struct file_operations fops = {
    .open = iut_open,
    .release = iut_release,
    .unlocked_ioctl = iut_ioctl, // can add read and write functions but is pointless
};
static int __init iut_init(void)
{
    major = register_chrdev(0, DEVICE_NAME, &fops);
    if (major < 0)
    {
        printk(KERN_ALERT "Device load failed!\n");
        return major;
    }
    printk(KERN_INFO "Device has been loaded: %d\n", major);
    return 0;
}
static void __exit iut_exit(void)
{
    unregister_chrdev(major, DEVICE_NAME);
    printk(KERN_INFO "Device module has been unloaded.\n");
}

module_init(iut_init);
module_exit(iut_exit);