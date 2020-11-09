// Space efficient implementation O(1) memory
int numIdenticalPairsSpace(int* nums, int numsSize){
    int counter = 0;
    for (int i = 0; i < numsSize; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            if (nums[i] == nums[j]) {
                counter++;
            }
        }
    }
    return counter;
}

// Time efficient implementation O(n) time
int numIdenticalPairsTime(int* nums, int numsSize){
    int hashTable[101] = { 0 };
    int counter = 0;
    
    for(int i = 0; i < numsSize; i++) {
        hashTable[nums[i]]++;
        if (hashTable[nums[i]] > 1) {
            counter += hashTable[nums[i]]-1;
        } 
    }
    return counter;
}
