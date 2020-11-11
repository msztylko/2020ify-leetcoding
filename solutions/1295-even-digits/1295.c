#include <stdbool.h>

bool hasEvenDigits(int n) {
    if (n / 10 == 0) return false;
    
    int counter = 0;
    while(n) {
        n /= 10;
        counter++;
    }
    return (counter % 2 ==0);
}


int findNumbers(int* nums, int numsSize) {
    int counter = 0;
    
    for (int i = 0; i < numsSize; i++) {
        if(hasEvenDigits(nums[i])) {
            counter++;
        }
    }
    return counter;
}
