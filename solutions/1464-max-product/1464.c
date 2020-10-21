int maxProduct(int *nums, int numsSize){
    long max = 0, product = 0;
    int i, j;
    
    for (i = 0; i < numsSize - 1; i++) {
        for (j = i + 1; j < numsSize; j++) {
            product = (nums[i]-1) * (nums[j]-1);
            if (product > max)
                max = product;
        }
    }
    return max;
}
