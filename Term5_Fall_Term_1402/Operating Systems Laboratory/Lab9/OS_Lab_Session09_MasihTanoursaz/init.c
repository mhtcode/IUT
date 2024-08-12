#include <stdio.h>
#include <unistd.h>
#include <sys/syscall.h>
#include <stdlib.h>

struct prc {
	pid_t id;
	char name[100];
};

int main()
{
	int number = 50000;
	struct prc *p;
	p = malloc(sizeof(struct prc) * number);
	while (1) {
		syscall(548, number, p);
		for (int i = 0; i < number; i++) {
			if (p[i].id == 0) {
				break;
			}
			printf("pid is %d, comm is %s\n", p[i].id, p[i].name);
		}
		fflush(stdout);
		sleep(5);
	}
	free(p);
	return 0;
}
