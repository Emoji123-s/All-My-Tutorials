/* Introducing the Zombie Process
In here, what happens when the child process terminates before the parent*/

#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>

int main(void)
{
    pid_t pid;
    /* Creating a child process*/
    pid = fork();

    /*If fork fails*/
    if (pid == -1)
    {
        perror("Unsuccessful\n");
        return (1);
    }

    /* In child process*/
    if (pid == 0)
    {
        printf("Child Process\n");
    }

    /* In Parent process*/
    else{
        sleep(30);
        printf("Parent Process\n");
    }
    return (0);
}

/* Why do we need to prevent the creaion of a zombie process?
There is one process table for each system, and the size of that table is finite. If too many zombie processes are generated, the table will be full. That is, the system would no longer generate new processes, then the entire system comes to a standstill
The wait() system call wais for a child process or any process in particular to change state. Include the <sys/types.h> and <sys/wait.h> header files. 
A changed state is considered to be:
1. The terminated child
2. The child was stopped by a signal
3. The child was resumed by a signal*/

#include <sys/wait.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>

int main(void)
{
    pid_t pid;
    /* Creating a child process*/
    pid = fork();

    /*If fork fails*/
    if (pid == -1)
    {
        perror("Unsuccessful\n");
        return (1);
    }

    /* In child process*/
    if (pid == 0)
    {
        printf("Child Process\n");
    }

    /* In Parent process*/
    else{
        wait(NULL);
        sleep(30);
        printf("Parent Process\n");
    }
    return (0);
}