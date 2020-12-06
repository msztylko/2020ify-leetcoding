int addDigits(int num) {
    int out;
    
    while(num / 10 != 0) {
        out = 0;
        while(num) {
            out += num % 10;
            num /= 10;
        }
        num = out;
    }
    return num;
}
