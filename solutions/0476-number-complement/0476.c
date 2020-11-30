int findComplement(int N) {
    if(N == 0) return 1;
    
    long mask = 1;
    
    while(mask <= N) {   
        N ^= mask;  
        mask <<= 1;  
    }
    return N;
}
