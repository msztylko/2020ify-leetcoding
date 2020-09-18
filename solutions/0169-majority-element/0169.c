// Brute-force solution
int majorityElementBF(int* nums, int numsSize)
{
    int majorityCounter = numsSize / 2;
    int i = 0;

    for (i = 0; i < numsSize; i++) {
        int element = nums[i];
        int counter = 0;
        int j = 0;

        for (j = 0; j < numsSize; j++) {
            if (element == nums[j]) {
                counter += 1;
            }
        }
        
        if (counter > majorityCounter) {
            return element;
        }
    } 
    
    return -1;
}

// interesting LC solution
int majorityElementLC(int* nums, int numsSize)
{
    int cnt = 0; 
    int res = 0;
    int i = 0;

    for (i = 0; i < numsSize; ++i) {
        if (cnt == 0) {
            res = nums[i];
        }
        if (res == nums[i]) {
            ++cnt;
        }
        else --cnt;
    }

    return res;
}
