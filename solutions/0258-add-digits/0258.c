int addDigits(int num) {
    if (num / 10 == 0) {return num;}
    
    int out;
    
    while (num / 10 != 0) {
        out = 0;
        do {
            out = out + num % 10;
            num /=10;
        } while(num);
        num = out;
    }
    return out;
}
