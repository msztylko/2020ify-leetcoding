void reverseString(char *s, int sSize) {
    int c, i, j;
    
    for (i = 0, j = sSize - 1; i < j; i++, j--) {
        c = s[i];
        s[i] = s[j];
        s[j] = c;
    }
}
