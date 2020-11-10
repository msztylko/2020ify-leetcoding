#include <math.h>

int isPrime(int num)
{
     if (num <= 1) return 0;
     if (num % 2 == 0 && num > 2) return 0;
     for(int i = 3; i < sqrt(num) + 1; i+= 2)
     {
         if (num % i == 0)
             return 0;
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

