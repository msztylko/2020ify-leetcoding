int countSegments(char * s) {
    int count = 0, inWord = 0;
    
    for (int i = 0; s[i]; i++) {
        if (s[i] != ' ') {
            if (inWord == 0) {
                count++;
                inWord = 1;
            } else {
                continue;
            }
        } else {
            inWord = 0;
        }
    }
    return count;
}
