/*Simple pid and ppid. pid stands for process id, and ppid stands for parent process id. A process is an instance of an executed program. When a program is compiled and executed, an instance of that file is taken and ran on the volatile memory, and with every process, a unique ID is given to it. If you run that file many times, and print out the pid, a new id would be allocated to it each time. Think of it this way, a father births a child, the father in this case is the parent process id, and the child is the process id. The father can give birth to a lot of processes, but he never changes, whereas for everytime a child(process) is born, a unique id is given to it. Just like how we humans have different fingerprints, taste sensations, face, hair color.... in the same way a process id is. Therefore, a parent process id stands for the prcess that creates a process you're processing/checking. And a process id can never change(except process 0).
To get a pid, use the getpid() function. It takes in no argument in the brackets
To get a ppid, use the getppid() function. Also takes in no argument in the brackets */

//Suppose we have an addition program, let's get the pid and the ppid of this program
#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>//The function we'll use is defined in this header. 

int main(void) //Function to take in no argument and return back an integer
{
    int a = 3;
    int b = 4;
    int c = 5;
    int sum = a + b;

    printf("Result is: %d\n", sum);

    // Now let's get the pid value
    //pid_t pid; pid_t is a defined function in unistd.h, and it is a signed integer type capable of representing a process id
    //pid = getpid();

    //printf("PID is: %u\n", pid);

    //Let's get the ppid
    pid_t ppid;
    ppid = getppid();
    printf("PPID is: %d\n", ppid);

    return (0);
}