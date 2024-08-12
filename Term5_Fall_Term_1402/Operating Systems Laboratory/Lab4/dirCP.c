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
		/****************STUDENTS******************/
			
	} else {  // in parent
		/****************STUDENTS******************/
		//wait & read status
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
    printf("Date\t\ttime\t\tExecution Time(ms)\tFile Name\n");
    
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
	      	/****************STUDENTS******************/
	      }
	    }
    }

    return 0;
}
