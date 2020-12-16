int hammingWeight(unsigned int n) {
    int weight = 0;
    
    while (n) {
        if (n & 1) {
            weight++;
        }
        n >>= 1;
    }
    return weight;
}
