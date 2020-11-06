#include <stdlib.h>

int* sortedSquares(int* A, int ASize, int* returnSize) {

    int* ans = calloc(ASize, sizeof(int));
    *returnSize = ASize;
    
    int i = 0; 
    int j = ASize - 1;
    int index = ASize - 1;
    
    while(i <= j) {
        if(-A[i] > A[j]) {
            ans[index--] = A[i] * A[i];
            i++;
        } else {
            ans[index--] = A[j] * A[j];
            j--;
        }
    }
    return ans;
}
