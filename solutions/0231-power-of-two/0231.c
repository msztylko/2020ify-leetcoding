#include <stdbool.h>

bool isPowerOfTwoNaive(int n){
    if (n < 1) return false;
    
    while(n != 1) {
        if (n % 2 != 0)
            return false;
        n /= 2;
    }
    return true;
}

bool isPowerOfTwoBit(int n) {
    if (n < 1) return false;
    
    if ((n & (n - 1)) == 0)
        return true;
    else
        return false;
}
