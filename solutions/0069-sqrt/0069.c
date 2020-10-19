int mySqrt(int x){
    if (x == 0 || x == 1) return x;

    long long int i = 1;
    long long sqrt = 1;
    while(sqrt <= x) {
        i++;
        sqrt = i*i;
    }
    return i -1;
}
