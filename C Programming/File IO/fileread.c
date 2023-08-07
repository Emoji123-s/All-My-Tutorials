#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void main()
{
    FILE *fp;
    fp = fopen("abc.txt", "r");
    /*r signifies that if that file exists, it shuld open it and allow users to write to it without erasing any of the content that file originally holds.
    If that file doesn't exist, it immediately produces an error, meaning that file has to be created before you can use the read operation*/

    if (fp == NULL)
    {
        printf("Error");
        exit(1);
    }

    /*To print a single character
    char ch;
    ch = fgetc(fp);
    printf("%c", ch);
    */

    /*Suppose i want to read the entire string
    We can add the above function into a while loop
    char ch;
    while (!feof(fp))
    {
        ch = fgetc(fp);
        printf("%c", ch);
    }
    */

    /*For String
    We use the fgets() function
    char str[50];
    fgets(str, 5, fp);
    printf("%s", str);
    //What would appear would be 4 characters, and then the last character would be allocated to the null character
    fclose(fp);
    */

    /*What if we had multiple lines in our text file?
    Ordinarily, the above function would only print the number of characters specified by the user. but if we move the above function to a while loop to print everything*/

    char ch[70];
    while (!feof(fp))
    {
        fgets(ch, 45, fp);
        printf("%s", ch);
    }
}