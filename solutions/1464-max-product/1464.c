int maxProductNaive(int *nums, int numsSize) {
    long max = 0, product = 0;
    int i, j;
    
    for (i = 0; i < numsSize; i++) {
        for (j = i + 1; j < numsSize; j++) {
            product = (nums[i]-1) * (nums[j]-1);
            if (product > max)
                max = product;
        }
    }
    return max;
}

int maxProductOnePass(int *nums, int numsSize) {
    int max = 0;
    int first = 0, second = 0;
    
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > first) {
            second = first;
            first = nums[i];
        } else if (nums[i] > second) {
            second = nums[i];
        }
    }
    max = (first-1) * (second-1); 
    return max;
}
