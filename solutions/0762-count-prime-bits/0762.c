#include <stdbool.h>

int countBits(int n) {
    int counter = 0;
    while(n) {
        if(n % 2 != 0) {
            counter++;
        }
        n /= 2;
    }
    return counter;
}

bool isPrime(int n) {
    if (n < 2) return false;
    int i = 0;
    
    for (i = 2; i < n; i++) {
        if (n % i == 0)
            return false;
    }
    return true;
}

int countPrimeSetBits(int L, int R){
    int counter = 0;
    int i;
    
    for (i = L; i <= R; i++) {
        int num_bits = countBits(i);
        if (isPrime(num_bits))
            counter++;
    }
    return counter;
}
