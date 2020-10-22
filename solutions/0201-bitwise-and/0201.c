int rangeBitwiseAndNaive(int m, int n){
    int out = m;
    for (int i = m; i < n; i++) {
        out &= (i+1);
    }
    return out;
}

int rangeBitwiseAndFast(int m, int n) {
    if (n > m)
        return rangeBitwiseAndFast(m/2, n/2);
    else
        return m;
}
