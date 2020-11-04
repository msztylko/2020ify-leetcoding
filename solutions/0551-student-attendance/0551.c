#include <string.h>
#include <stdbool.h>

bool checkRecord(char * s) {
    int Acounter = 0;
    int length = strlen(s);
    
    for (int i = 0; i < length; i++) {
        if (s[i] == 'A')
            Acounter++;
        if (s[i] == 'L') {
            if (i + 2 < length && s[i+1] == 'L' && s[i+2] == 'L')
                return false;
        }
    }
    return (Acounter > 1) ? false : true;
}
