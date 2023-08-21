/* The getlne() function reads input or an entire line from stream, stoing the address of the buffer containing the text into *lineptr. The buffer is null terminated and includes he newline character, if one was found. It is defined in the <stdio.h> header, and it is basically used as a delimited string input
The syntax is
        ssize_t getline(char **lineptr, size_t *n, FILE *stream);
It has 3 parameters
1. Double pointer to a char
2. Pointer to a size_t datatype
3. A file pointer

A stream helps us specify where we'll read our text from. So if we specify the standard input, the getline() function will retrieve the text from our keyboard. Usually, when it is retrieved, it is stored in a buffer, either by you, or by the getline function. But the size of the buffer created will be stored in the variable n (ie, size_t *n). Then the lineptr sizes the address of the buffer that was created*/


#define _GNU_SOURCE 

#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    size_t n = 10;
    char *buf = malloc(sizeof(char) *n);

    if (buf == NULL) 
    {
        printf("Memory allocation failed\n");
        return 1;
    }

    printf("Enter name: ");
    getline(&buf, &n, stdin);

    printf("Name is %s Buffer size is %zu\n", buf, n);

    free(buf);
    return (0);
}

/* If for instance, a name like "Jack" is inputed, the allocated space will contain that name. But if a longer name is inputed, the buffer space automatically increases. If the buffer is not large enough to hold the line, getline() resizes it with realloc(3), updating *lineptr and *n as necessary
With getline(), you could always skip the malloc function, and getline wuld automatically allocate space for the buffer, and all we have to do id to free the allocated buffer. */

#define _GNU_SOURCE 

#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    size_t n = 10;
    char *buf = NULL;

    if (buf == NULL) 
    {
        printf("Memory allocation failed\n");
        return 1;
    }

    printf("Enter name: ");
    getline(&buf, &n, stdin);

    printf("Name is %s Buffer size is %zu\n", buf, n);

    free(buf);
    return (0);
}

/* If *lineptr is NULL, then getline() will allocate a buffer for storing the line, which should be freed, by the user program.*/