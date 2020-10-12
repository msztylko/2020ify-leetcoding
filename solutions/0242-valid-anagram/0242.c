#include <stdbool.h>
#include <string.h>

bool isAnagram(char *s, char *t)
{
    int s_count[26] = {0}, t_count[26] = {0};
    int i, slen = strlen(s), tlen = strlen(t);
    
    for (i = 0; i < slen; i++) {
        int c = s[i] - 'a';
        s_count[c] += 1;
    }
    
    for (i = 0; i < tlen; i++) {
        int c = t[i] - 'a';
        t_count[c] += 1;
    }
    
    for (i = 0; i < 26; i++) {
        if (s_count[i] != t_count[i])
            return false;
    }
    
    return true;
}
