//This program is to read a character from the user and print its ASCII value. 
//ASCII stands for American Standard Code for Information Interchange. Basically like a morse code of some sort(to which I'll still learn :) ). It is a standard data-encoding format for electronic communication between computers. ASCII assigns standard numeric values to letters, numerals, punctuation marks, and other characters used in computers.)

#include <stdio.h>

int main(void)
{
    char usr_char[3];
    char ch; // char is more cohesive since the user might put in a value to bring out an integer, or a symbol. Whereas int would only produce integer values. Plus the question says "Read a character" :D 

    printf("Enter a value: \n");
    scanf("%c %c", &usr_char, &ch); //The trailing whitespace ensures that scanf doesnt read any unintended characters. It is necessary to consume any whitespace left in the newline. Although you can choose to add a whitespace or not, it would run either way. So it can be scanf(" %c", &usr_char);- ChatGPT

    printf("ASCII Value of %c is: %d\n", usr_char, ch); //One character goes for the %c, while the other goes for %d

    return (0);
}

//Really thought it was going to be harder than this