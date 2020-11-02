#include <stdbool.h>
#include <string.h>

bool detectCapitalUse(char * word) {
    if (strlen(word) == 1) { return true; }
    
    int i, small = 0, big = 0;
    
    for(i = 0; word[i]; i++) {
        if (word[i]>='a' && word[i] <='z')
            small++;
        if (word[i]>='A' && word[i] <='Z')
            big++;
    }
    
    if (small == 0 && big != 0)
        return true;
    else if (big == 0 && small != 0)
        return true;
    else if (big == 1 && word[0]>='A' && word[0] <='Z')
        return true;
    else 
        return false;
}
