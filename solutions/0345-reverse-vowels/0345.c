#include <string.h>
#include <stdbool.h>

bool isVowel(char letter) {
    if (letter == 'e' ||
        letter == 'i' ||
        letter == 'o' ||
        letter == 'u' ||
        letter == 'a' ||
        letter == 'E' ||
        letter == 'I' ||
        letter == 'O' ||
        letter == 'U' ||
        letter == 'A') {
        return true;
    } else {
        return false;
    }
}

char *reverseVowels(char * s) {
    int start = 0;
    int end = strlen(s) - 1;
    
    while (start < end) {
        if (isVowel(s[start]) && isVowel(s[end])) {
            char temp = s[start];
            s[start] = s[end];
            s[end] = temp;
            end--;
            start++;
        } else if (isVowel(s[start])) {
            end--;
        } else if (isVowel(s[end])) {
            start++;
        } else {
            end--;
            start++;
        }
    }
    return s;
}
