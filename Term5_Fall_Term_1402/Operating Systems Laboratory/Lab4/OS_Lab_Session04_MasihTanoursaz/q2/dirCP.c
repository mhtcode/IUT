#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/time.h>
#include <sys/wait.h>
#include <time.h>
#include <dirent.h> 
#include <stdio.h>
#include <string.h>


void childWork(char src[],char dst[])
{
	pid_t pid;
	pid = fork();
	if( pid == 0){  // in child
		/****************STUDENTS******************/
		//run cp
		execlp("cp", "cp", src, dst, NULL);
		/****************STUDENTS******************/
			
	} else {  // in parent
		/****************STUDENTS******************/
		//wait & read status
		int status;
		waitpid(pid, &status, 0);
		if(WIFEXITED(status) && WEXITSTATUS(status) !=0)
			printf("Error occured\nstatus code is:%d\n", status);
		/****************STUDENTS******************/
	}	
}

int main(int argc , char* argv[])
{
    if(argc!=3){
    	printf("Parameters Error\n");
    	return 0;
    }
    struct timeval start,stop;
    printf("Date\t\t\ttime\t\tExecution Time(ms)\tFile Name\n");
    
    DIR *d;
    struct dirent *file;
    d = opendir(argv[1]);
    
    if (d) {
	    while ((file = readdir(d)) != NULL) {
	      if(file->d_type == DT_REG){
	      	
	      	char srcPath[512],dstPath[512];
	      	sprintf	(srcPath,"%s/%s",argv[1],file->d_name);
	      	sprintf	(dstPath,"%s/%s",argv[2],file->d_name);
	      	
	      	/****************STUDENTS******************/
			//call childWork and measure the time
			gettimeofday(&start, NULL);
			childWork(srcPath, dstPath);
			gettimeofday(&stop, NULL);
			long sec = stop.tv_sec - start.tv_sec;
			float us = stop.tv_usec - start.tv_usec;
			long diffrenceTime = sec * 1000 + us/1000.0;

			time_t now;
			struct tm *timeInfo;
			time(&now);
			timeInfo = localtime(&now);
			int year = timeInfo->tm_year + 1900;
			int month = timeInfo->tm_mon + 1;
			int day = timeInfo->tm_mday;
			int hour = timeInfo->tm_hour;
			int minute = timeInfo->tm_min;

			printf("---------------------------------------------------------------------------------\n");
			printf("%d-%02d-%02d\t\t%02d:%02d\t\t%ld\t\t\t%s\n", year, month, day, hour, minute, diffrenceTime, file->d_name);
			
	      	/****************STUDENTS******************/
	      }
	    }
    }

    return 0;
}
