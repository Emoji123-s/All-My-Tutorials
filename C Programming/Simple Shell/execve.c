/* The execve means execute programs. It is defined in the <unistd.h> header file. It executes programs provided it is a binary executable or a script starting with the line of form 
        #! interpreter [optional-arg]
Execve doesn't return on success, and the text, data, bss, and satck of the calling process are overwritten by that of the program loaded.
It accepts 3 parameters
        int execve(const char *filename), char *const argv[], char *const envp[]; 
1. The filename
2. The argument, or an array of arguments
3. The environment variable

Supposing i want to print the files in my working directory as a long format.... Ordinarliy, an ls would be used, but we can also use the execve command to do that*/

#include <stdio.h>
#include <unistd.h>
int main(void)
{
    char *argv[] = {"/bin/ls", "-l", NULL};

    int val = execve(argv[0], argv, NULL);
    if (val == -1)
    {
        perror("Unsuccessful\n");
    }
    printf("Done with execve\n");

    return (0);
}

/* Argv is an array of argument strings passed to the new program. By convention, the first of these strings should contain the filename associated with the file being executed. 
       char *argv[] = {"/bin/ls", "-l", NULL}; means
We are creating a pointer argv[] ie, an array of arguments, that executes the ls function stred in the binary directory ls. Since we want that in long format, we add another argument -l and both argv and envp must be terminated with a null pointer.
The return value of execve is nothing, and if unsuccessful, it return -1. To check, we use an if statement should incase it fails to execute. */

#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
int main(void)
{
    pid_t pid;
    char *argv[] = {"/bin/ls", "-l", NULL};

    pid = fork();
    if (pid == -1)
    {
        return (-1);
    }

    if (pid == 0)
    {
        int val = execve(argv[0], argv, NULL);
        if (val == -1)
        {
            perror("Unsuccessful\n");
        }
    }
    else
    {
        wait(NULL);
        printf("Done with execve\n");
    }

    return (0);
}