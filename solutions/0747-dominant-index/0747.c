int dominantIndex(int* nums, int numsSize) {
    
    int index = 0, first = 0, second = 0;
    
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > first) {
            second = first;
            first = nums[i];
            index = i;
        } else if (nums[i] > second) {
            second = nums[i];
        }
    }
    
    if (first >= 2*second)
        return index;
        
    return -1;
}
