#include <stdio.h>
#include <string.h>

void reverseString(char* s, int sSize){
    char *startPtr = s;
    char *endPtr = s + sSize - 1;
    char temp;

    while(startPtr < endPtr) {
        temp = *endPtr;
        *endPtr = *startPtr;
        *startPtr = temp;    
        startPtr++;
        endPtr--;
    }
};

// int main(void) 
// {
//     char str1[] = "hello";
//     int sSize1 = strlen(str1);
//     printf("%s\n", str1);
//     reverseString(str1, sSize1);
//     printf("%s\n", str1);
// 
//     char str2[] = "Hannah";
//     int sSize2 = strlen(str2);
//     printf("%s\n", str2);
//     reverseString(str2, sSize2);
//     printf("%s\n", str2);
// }
