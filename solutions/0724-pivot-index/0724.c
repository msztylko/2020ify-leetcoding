int pivotIndex(int* nums, int numsSize) {
    if (numsSize == 0) return -1;
    
    int sum = 0, leftSum = 0, rightSum;
    
    for (int i = 0; i < numsSize; i++) {
        sum  += nums[i];
    }
    
    for (int i = 0; i < numsSize; i++) {
        rightSum = sum - leftSum - nums[i];
        if(leftSum == rightSum)
            return i;
        leftSum += nums[i];
    }
    return -1;
}
