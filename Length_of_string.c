#include <stdio.h>
#include <string.h>

int main() {
    char s[100];
    int length=0;

    printf("Enter a string : ");
    scanf("%s",s);

    while (s[length] != '\0') {
        length++;
    }

    printf("The length of the string is %d",strlen(s));
}