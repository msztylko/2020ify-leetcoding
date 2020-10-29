#include <stdbool.h>

bool isPalindrome(int x){
    if (x < 0) { return false; }
    
    long val = 0, original = x;
    
    do {
        val = val * 10 + x % 10;
        x /= 10;
    } while(x);
    
    return val == original;
}
