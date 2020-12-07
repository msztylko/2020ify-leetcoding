int maxPower(char * s) {
    int counter = 1, max = 1;
    
    for (int i = 1; s[i]; i++) {
        if (s[i-1] == s[i]) {
            counter++;
            if (counter > max)
                max = counter;
        }
        else {
            counter = 1;
        }
    }
    return max;
}
