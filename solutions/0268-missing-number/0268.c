int missingNumber(int* nums, int numsSize){
    int max = -1;
    int sum = 0;
    int bound = 1;
    
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == numsSize)
            bound = 0;
        if (nums[i] > max)
            max = nums[i];
        sum += nums[i];
    }
    if (bound == 1)
        return numsSize;
    else
        return ((max * (max + 1)) / 2) - sum;
}
