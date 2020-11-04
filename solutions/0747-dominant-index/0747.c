int dominantIndex(int* nums, int numsSize){
    int max = 0;
    int index = 0;
    
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > max) {
            max = nums[i];
            index = i;
        }
    }
    
    for (int i = 0; i < numsSize; i++) {
        if (index != i && nums[index] > 2*nums[i]) {
            continue;
        } else if (index != i && nums[index] < 2*nums[i]) {
            return -1;
        }
    }
    return index;
}
            
