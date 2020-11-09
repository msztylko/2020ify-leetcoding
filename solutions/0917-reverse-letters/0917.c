#include <stdio.h>
#include <string.h>
#define ASCIIA 65
#define ASCIIz 122

char * reverseOnlyLetters(char * S) {
    char *out = S;
    for (int i = 0; S[i]; i++) {
        out[i] = S[i];
    }
    
    int start = 0;
    int end = strlen(out) - 1;

    while (start < end) {
        if (out[start] <= 96 && out[start] >= 91) {
            start++;
        } else if (out[end] <= 96 && out[end] >= 91 ) {
            end--; 
        }else if (out[start] >= ASCIIA && out[start] <= ASCIIz && out[end] >= ASCIIA && out[end] <= ASCIIz) {
            char tmp = out[end];
            out[end--] = out[start];
            out[start++] = tmp;
        } else if (out[start] < ASCIIA || out[start] > ASCIIz) {
            start++;
        } else if (out[end] < ASCIIA || out[end] > ASCIIz ) {
            end--;
        } else {
            start++;
            end--;
        }
    }
    return out;
}
