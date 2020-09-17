int singleNumber(int *nums, int numsSize) 
{
    int i = 0;
    int out = 0;
    
    for (i = 0; i < numsSize; i++) {
        out ^= nums[i];
    }

    return out;
}
