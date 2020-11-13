#include <stdlib.h>

int* sortArrayByParity(int* A, int ASize, int* returnSize) {
    *returnSize = ASize;
    if (A == NULL) return NULL;
    if (ASize == 1) return A;
    
   int i = 0, j = ASize - 1;
    while (i < j) {
        if (A[i] % 2 > A[j] % 2) {
            int tmp = A[i];
            A[i] = A[j];
            A[j] = tmp;
        }

        if (A[i] % 2 == 0) i++;
        if (A[j] % 2 == 1) j--;
    }

    return A;
    
}
