int fib(int N) {
    if (N == 0) { return 0; }
    if (N == 1) { return 1; }
    
    return fib(N-1) + fib(N-2);
}

int fibArray(int n) {
    
    int F[31] = {0};
    F[0] = 0;
    F[1] = 1;
    
    for (int i = 2; i <= n; i++) {
        F[i] = F[i-2] +  F[i-1];
    }
    
    return F[n];
}
