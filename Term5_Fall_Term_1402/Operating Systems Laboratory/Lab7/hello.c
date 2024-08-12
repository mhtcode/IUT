<<<<<<< HEAD
#include <linux/init.h>
#include <linux/module.h>
MODULE_LICENSE(“GPL”);
MODULE_AUTHOR(“OSLAB”);
static int hello_init(void){
	printk(KERN_ALERT “Hello world!\n”);
	return 0;
}
static void hello_exit(void){
	printk(KERN_ALERT “Goodbyte cruel world\n”);
}
module_init(hello_init);
=======
#include <linux/init.h>
#include <linux/module.h>
MODULE_LICENSE(“GPL”);
MODULE_AUTHOR(“OSLAB”);
static int hello_init(void){
	printk(KERN_ALERT “Hello world!\n”);
	return 0;
}
static void hello_exit(void){
	printk(KERN_ALERT “Goodbyte cruel world\n”);
}
module_init(hello_init);
>>>>>>> 10f5617 (Term 5 Completed)
module_exit(hello_exit);