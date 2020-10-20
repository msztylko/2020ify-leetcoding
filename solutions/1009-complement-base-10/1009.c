int bitwiseComplement(int N){
    if(N == 0) return 1;
    
    long ret = N;
    long mask = 1;
    
    while(mask <= ret) {   
        ret = ret ^ mask;  
        mask = mask << 1;  
    }
    return ret;
}
