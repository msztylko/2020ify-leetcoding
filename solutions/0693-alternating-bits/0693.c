#include <stdbool.h>

bool hasAlternatingBits(int n) {
    int last = n % 2, rest = n / 2;
    
    while (last <= rest) {
        if (last == (rest % 2)) {
            return false;
        } else {
            last = rest % 2;
            rest /= 2;
        }
    }
    return true;
}
