int mySqrt(int x) {
    long i = 1, sqrt = 1;
        
    while(sqrt <= x) {
        i++;
        sqrt = i*i;   
    }
    return i -1;
}
