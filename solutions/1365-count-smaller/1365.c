#include <stdlib.h>

int* smallerNumbersThanCurrent(int* nums, int numsSize, int* returnSize) {
    int *ans = malloc(sizeof(int) * numsSize);
    *returnSize = numsSize;
    int counter;
    
    for (int i = 0; i < numsSize; i++) {
        counter = 0;
        for (int j = 0; j < numsSize; j++) {
            if (j != i && nums[j] < nums[i])
                counter++;
        }
        ans[i] = counter;
    }
    return ans;
}
