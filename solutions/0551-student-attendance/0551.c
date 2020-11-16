#include <stdbool.h>

bool checkRecord(char *s) {
    int a = 0, l = 0;
    for(int i = 0; s[i]; i++) {
        if(s[i] == 'A') 
            a++;
        if(s[i] == 'L') 
            l++;
        else 
            l = 0;
        if(a >= 2 || l > 2) 
            return false;
    }
    return true;
}
