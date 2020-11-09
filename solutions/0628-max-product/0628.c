#include <limits.h>

int max(int num1, int num2) {
    return (num1 > num2 ) ? num1 : num2;
}

int min(int num1, int num2) {
    return (num1 > num2 ) ? num2 : num1;
}

int maximumProduct(int *nums, int numsSize) {
    int f[2][4], i, j;
    f[0][0] = f[1][0] = 1;
    for (j = 3; j > 0; --j) {
        f[0][j] = INT_MIN;
        f[1][j] = INT_MAX;
    }        
        
    for (i = 0; i < numsSize; ++i) {
        for (j = 3; j > 0; --j) {
            if (f[0][j - 1] == INT_MIN) {
                continue;
            }
            f[0][j] = max(f[0][j], max(f[0][j - 1] * nums[i], f[1][j - 1] * nums[i]));
            f[1][j] = min(f[1][j], min(f[0][j - 1] * nums[i], f[1][j - 1] * nums[i]));
        }
    }                              
    return f[0][3];
}
