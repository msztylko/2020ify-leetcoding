int findComplement(int N) {
    if(N == 0) return 1;
    
    int ret = N;
    long mask = 1;
    
    while(mask <= ret) {   
        ret ^= mask;  
        mask <<= 1;  
    }
    return ret;
}
