#include <linux/kernel.h>
#include <linux/syscalls.h>
#include <linux/sched.h>
#include <asm/uaccess.h>
struct task_struct *task;

struct prc {
	pid_t id;
	char name[100];
};

SYSCALL_DEFINE2(hello, int, number, long, adres)
{
	long int counter = 0;
	int num_prc = 0;
	struct prc *p;
	p = (struct prc *)adres;
	for_each_process (task) {
		num_prc++;
	}
	int num2 = num_prc + 1;
	p[num2].id = 0;
	for_each_process (task) {
		p[counter].id = task->pid;
		strcpy(p[counter].name, task->comm);
		counter++;
		if (num_prc == counter || counter == number)
			return 0;
	}
	return 0;
}
