#include <stdbool.h>
bool isBadVersion(int version);

int firstBadVersionLinear(int n) {
    for (int i = 1; i <=n; i++ ) {
        if (isBadVersion(i)) {
            return i;
        }
    }
    return -1;
}

int firstBadVersion(int n) {
    int low = 1, high = n, mid;
    
    while (low <= high) {
        mid = low + (high - low) / 2;
        if (isBadVersion(mid)) {
            if (mid > 1 && !isBadVersion(mid - 1)) {
                return mid;
            } else {
                high = mid - 1;    
            }
        } else {
            low = mid + 1;
        }
    }
    return mid;
}
