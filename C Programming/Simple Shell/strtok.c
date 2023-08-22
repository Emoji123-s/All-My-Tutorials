/* The strtok unction takes strings and breaks them down into token. Basically like a tokenizer. It is useful  when you want to specify which part of a string is an argument, and which is a function. Example
                    ls -la
Ordinarily, the getline() function would read the string ully and execute it, but with the strtok function, i breaks down the string, as ls into function, and -la as an argument.
The main function of strtok is to extract tokens from strings. It is defined in the <string.h> header file, and the syntax is
            char *strtok(char *str, const char *delim);
The delim means delimeter, and it is one or more characters that seperates text strings*/
/*
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
    char str[] = "Jesus loves you";
    char *delim = " ";
    char *token;

    token = strtok(str, delim);
    printf("%s", token);

    return (0);
}
*/
/* With the above code, only Jesus should be printed. But what if we want to print he entire string?
On the first call to strtok, the string to be parsed should be specified in str. In each subsequent call that should parse the same string, str must be NULL,  */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
    char str[] = "Jesus loves you";
    char *delim = " ";
    char *token;

    token = strtok(NULL, delim);
    printf("%s", token);

    return (0);
}

/* We can use a while loop. With this, we can take advantage of the return value of the strtok function, which returns a pointer to the next token, or NULL if there are no more tokens*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
    char str[] = "Jesus loves you";
    char *delim = " ";
    char *token;

    token = strtok(str, delim);

    while (token)
    {
        printf("%s\n", token);
        token = strtok(NULL, delim);
    }
    return (0);
}

/* If we change the array of characters to a string literal i.e
                char *str = "Jesus loves you;"
Once compiled, a segmentation fault will be met. But we can tweak the code to make it work, by allocating memory on the heap*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
    char *src = "Jesus loves you";
    char *str = malloc(sizeof(char)= strlen(src));
    char *delim = " ";
    char *token;

    strcpy(str,src);
    token = strtok(str, delim);

    while (token)
    {
        printf("%s\n", token);
        token = strtok(NULL, delim);
    }
    return (0);
}