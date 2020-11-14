#include <string.h>
#include <ctype.h>

char *reverseOnlyLetters(char * S) {
    for (int i = 0, j = strlen(S) -1; i < j;) {
        if (!isalpha(S[i]))
            i++;
        else if (!isalpha(S[j]))
            j--;
        else {
            char tmp = S[j];
            S[j--] = S[i];
            S[i++] = tmp;
        }
            
    }
    return S;
}
