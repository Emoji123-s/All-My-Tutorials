/* A C program to take in 2 integers and prints their sum */

#include <stdio.h>

int main(void)
{
    int a;
    int b;
    int sum; /* Variable to hold the result of the addition*/
    printf("Enter 2 numbers:\n ");
    scanf("%d %d", &a, &b);

    sum = a + b;

    printf("Result is %d\n", sum);

    return (0);
}

/* Another Way using declared prototypes */
