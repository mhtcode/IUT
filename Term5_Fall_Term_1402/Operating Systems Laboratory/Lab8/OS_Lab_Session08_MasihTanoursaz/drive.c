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
#define DEVICE_NAME "myWallet"

static int major;

static char password[10] = "1234";
static int isLock = 1;
static char MESSAGE[64] = "Masih Tanoursaz 40006133";

static long wIoctl(struct file *file, unsigned int req, unsigned long pointer)
{
	struct iut_data *data;
	data = kzalloc(sizeof(struct iut_data), GFP_KERNEL);
	if (!data)
		return -ENOMEM;
	if (copy_from_user(data, (void *)pointer, sizeof(struct iut_data)))
		return -EFAULT;
	switch (req)
	{
	case getStatus:
		if (isLock == 1)
			printk(KERN_INFO "Get status: %s\n", "isLocked");
		else
			printk(KERN_INFO "Get status: %s\n", "notLocked");
		break;
	case changeStatus:
		printk("in change satatus, islock: %d\n", isLock);
		if (isLock)
		{
			if (strcmp(password, data->password))
			{
				strcpy(data->data, "Fail to change status: Invalid password");
				printk(KERN_ALERT "Fail to change status: Invalid password");
				if (copy_to_user((struct iut_data *)pointer, data, sizeof(struct iut_data)))
					return -EFAULT;
				return -EINVAL;
			}
			else
			{
				isLock = 0;
				strcpy(data->data, "Now Device successfully unlocked.");
				printk(KERN_INFO "Now Device successfully unlocked.");
				break;
			}
		}

		isLock = 1;
		strcpy(data->data, "Now Device successfully locked.");
		printk(KERN_INFO "Now Device successfully locked.");
		break;

	case changePass:
		if (strlen(data->new_password) > 10 || strcmp(password, data->password))
		{
			strcpy(data->data, "Fail to change password: Invalid password (Wrong or long)");
			printk(KERN_ALERT "Fail to change password: Invalid password (Wrong or long)");
			if (copy_to_user((struct iut_data *)pointer, data, sizeof(struct iut_data)))
				return -EFAULT;
			return -EINVAL;
		}

		strcpy(data->data, "Password changes successfully.");
		printk(KERN_INFO "Password changes successfully.");
		strcpy(password, data->new_password);
		break;

	case getContent:
		if (strcmp(password, data->password))
		{
			strcpy(data->data, "Unable to retrive the secret: Password is wrong.\n");
			printk(KERN_ALERT "Unable to retrive the secret: Password is wrong.\n");
			if (copy_to_user((struct iut_data *)pointer, data, sizeof(struct iut_data)))
				return -EFAULT;
			return -EINVAL;
		}

		strcpy(data->message, MESSAGE);
		printk(KERN_INFO "Get content.");
		strcpy(password, data->new_password);
		break;
	}

	return 0;
}

static int wOpen(struct inode *inode, struct file *file)
{
	printk(KERN_INFO "MyWallet opened.\n");
	isLock = 1;
	return 0;
}
static int wRelease(struct inode *inode, struct file *file)
{
	printk("device closed\n");
	return 0;
}

static ssize_t wRead(struct file *filep, char *buffer, size_t len, loff_t *offset)
{
	int errors = 0;

	if (isLock == 1)
	{
		printk(KERN_ALERT "Unable to retrive the secret: Device is locked.\n");
		return -EACCES;
	}

	MESSAGE[strlen(MESSAGE)] = '\0';
	errors = copy_to_user(buffer, MESSAGE, strlen(MESSAGE) + 1);

	if (errors == 0)
	{
		printk(KERN_INFO "Secret retrived successfully");
		return strlen(MESSAGE);
	}

	return -EFAULT;
}

static ssize_t wWrite(struct file *filep, const char *buffer, size_t len, loff_t *offset)
{
	int errors = 0;

	if (isLock == 1)
	{
		printk(KERN_ALERT "Unable to change the secret: Device is locked.\n");
		return -EACCES;
	}

	if (len > 64)
	{
		printk(KERN_ALERT "The size of input is so large.\n");
		return -EINVAL;
	}

	errors = copy_from_user(MESSAGE, buffer, len);

	if (errors == 0)
	{
		printk(KERN_INFO "Change the content to : \"%s\"\n", MESSAGE);
		return strlen(MESSAGE);
	}

	return -EFAULT;
}
static struct file_operations fops = {
	.open = wOpen,
	.read = wRead,
	.write = wWrite,
	.release = wRelease,
	.unlocked_ioctl = wIoctl,
};
static int __init iut_init(void)
{
	major = register_chrdev(0, DEVICE_NAME, &fops);

	if (major < 0)
	{
		printk(KERN_ALERT "MyWallet load failed.\n");
		return major;
	}

	printk(KERN_INFO "MyWallet module loaded: %d\n", major);
	isLock = 1;
	return 0;
}

static void __exit iut_exit(void)
{
	unregister_chrdev(major, DEVICE_NAME);
	printk(KERN_INFO "MyWallet module unloaded.\n");
}

module_init(iut_init);
module_exit(iut_exit);

MODULE_LICENSE("GPL");
