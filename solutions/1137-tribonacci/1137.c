#define MAX 37

int tribonacci_array(int n) {
    int i, T[MAX+1] = {0};
    
    T[0] = 0;
    T[1] = 1;
    T[2] = 1;
    
    for (i = 3; i <= n; i++) {
        T[i] = T[i-1] + T[i-2] + T[i-3];
    }
    
    return T[n];
}

int tribonacci(int n) {
    if (n == 0) { return 0; }
    if (n == 1 || n == 2) { return 1;}
    
    int a = 0, b = 1, c = 1, d;
    
    for (int i = 2; i < n; i++) {
        d = a + b + c;
        a = b;
        b = c;
        c = d;
    }
    return d;
}
