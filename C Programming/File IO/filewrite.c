#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void main()
{
    FILE *fp; //Pointer to point to the file
    fp = fopen("def.txt", "w");
    /* w signifies that if that file exists, then the content of that file would be completely erased. A cpy of that file would be opened in the volatile memory(RAM). Once done with the file, the copy would be returned back to the original file
    If the file doesn't exist, that file would be created, a copy would be opened in the volatile memory(RAM), and once done, the copy would be returned to the original file.*/
    if (fp == NULL)
    {
        printf("Invalid File");
        exit(1);
    }

    /* Suppose i want to add a character
    char ch = 'a';
    fputc(ch, fp);
    */

    /* Suppose i want to add a string
    char ch[50] = "Isaac-Victor Providence";
    fputs(ch, fp);
    */

    /*Suppose i want to print different formatted datatypes*/
    char ch[50] = "Isaac-Victor Providence";
    int a = 10;
    fprintf(fp, "%s %d", ch, a);

    fclose(fp);
}