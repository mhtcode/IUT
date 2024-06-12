#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <signal.h>
#include <time.h>

void handler(int signo)
{
	switch (signo)
	{
	case SIGALRM:
		printf("I received alarm. \n");
		break;
	}
}

int main()
{
	struct sigaction action1;
	action1.sa_handler = handler;
	action1.sa_flags = 0;
	sigemptyset(&action1.sa_mask);

	if (sigaction(SIGALRM, &action1, NULL) == -1)
	{
		perror("Signal");
		return EXIT_FAILURE;
	}
	alarm(5);
	while (1)
	{
		printf("I am alive.\n");
		sleep(1);
	}
	return 0;
}
