#include <math.h>

int isPrime(int n)
{
    int i = 0;
    int square_n = (int)sqrt(n) + 1;
    
    if (n == 0 || n == 1) {
        return 0;
    }
    
    for (i = 2; i < square_n; i++) {
        if (n % i == 0) {
            return 0;
        }   
    }
    
    return 1;
}

int countPrimes(int n)
{
    int counter = 0;
    int i = 0;
    
    for (i = 0; i < n; i++) {
        if(isPrime(i)) {
            counter++;
        }
    }
    return counter;
}

