int countSegments(char * s) {
    int counter = 0;
    int inWord = 0;
    
    for (int i = 0; s[i]; i++) {
        if (s[i] != ' ') {
            if (inWord == 0)
                counter++;
            inWord = 1;
        } else {
            inWord = 0;
        }
    }
    return counter;
}
