#include <stdbool.h>
#include <stdlib.h>

bool isSelfDividing(int n) {
    int digit, num = n;
    
    while(n) {
        digit = n % 10;
        if (digit == 0)
            return false;
        else if (num % digit != 0)
            return false;
        n /= 10;
    }
    return true;
}

int* selfDividingNumbers(int left, int right, int* returnSize) {
    int index = 0;
    int counter = 0;
    
    for (int i = left; i <= right; i++) {
        if (isSelfDividing(i))
            counter++;
    }
    
    int *ans = malloc(sizeof(int) * counter);
    *returnSize = counter;
    for (int i = left; i <= right; i++) {
        if (isSelfDividing(i))
            ans[index++] = i;
    }
    return ans;
}
