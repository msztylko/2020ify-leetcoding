int xorOperation(int n, int start) {
    int out = start;
        
    for (int i = 1; i < n; i++) {
        int elem = start + 2*i;
        out ^= elem;
    }
    return out;
}
