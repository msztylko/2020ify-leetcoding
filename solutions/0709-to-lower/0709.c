char * toLowerCase(char * str) {
    for (int i = 0; str[i]; i++) {
        if (str[i] >= 65 && str[i] <= 90)
            str[i] += 32;
    }
    return str;
}
