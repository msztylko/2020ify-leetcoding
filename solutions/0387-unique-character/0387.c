int firstUniqChar(char * s) {
    int h[26] = {0};
    
    for(int i = 0; s[i]; i++) {
        h[s[i] - 'a']++;
    }
    
    for(int i = 0; s[i]; i++) {
        if (h[s[i] - 'a'] == 1) 
            return i; 
    }
    return -1;
}
