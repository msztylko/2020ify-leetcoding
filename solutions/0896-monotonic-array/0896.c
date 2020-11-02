#include <stdbool.h>

bool isMonotonic(int* A, int ASize) {
    
    int increasing = 1, decreasing = 1;
    
    for (int i = 0; i < ASize-1; i++) {
        if (A[i] < A[i+1]) {
            decreasing = 0;
        } else if (A[i] > A[i+1]) {
            increasing = 0;
        }
    }
    return (increasing || decreasing);
}
