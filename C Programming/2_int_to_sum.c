// A C program to take in 2 integers and prints their sum
/*
#include <stdio.h>

int main(void)
{
    int a;
    int b;
    int sum; // Variable to hold the result of the addition
    printf("Enter 2 numbers:\n ");
    scanf("%d %d", &a, &b);

    sum = a + b;

    printf("Result is %d\n", sum);

    return (0);
}
*/
/* Another Way using declared prototypes. With this, numbers are already specified, so it'll automatically print them
#include "main.h"
#include <stdio.h>

int main(void)
{
    int result = 0;
    result = add(6, 8);

    printf("Sum is: %d\n", result);

    return(0);
}
*/

//Using Conditions
#include <stdio.h>

int main(void)
{
    //We want a situation where the user can answer either yes or no, and then a particular function depending on that answer will run
    int num1, num2, sum; //Variables to hold the values the user inputs
    char choice; //As the variable to loop through
    do
    {
    
        printf("Welcome to your personal Adder\n");

        printf("Enter the first value: \n");
        scanf("%d", &num1);

        printf("Enter the second number: \n");
        scanf("%d", &num2);

        sum = num1 + num2;
        printf("The sum is: %d\n", sum);

        printf("Would you like to perform another addition? (Y/N): ");
        
        scanf(" %c", &choice);

    } while (choice == 'Y' || choice == 'y');
        
    printf("Thank you for using the program :)\n");
    return (0);
}