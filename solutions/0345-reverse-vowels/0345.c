#include <stdbool.h>
#include <string.h>

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

char * reverseVowels(char * s) {
    int start = 0;
    int end = strlen(s) - 1;
    
    while (start < end) {
        if (!isVowel(s[start]))
            start++;
        else if (!isVowel(s[end]))
            end--;
        else {
            char temp = s[start];
            s[start++] = s[end];
            s[end--] = temp;
        }
    }
    return s;
}
