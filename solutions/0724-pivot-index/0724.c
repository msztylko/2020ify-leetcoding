int leftSum(int index, int* arr) {
    int sum = 0;
    for (int i = 0; i < index; i++)
        sum += arr[i];
    return sum;
}

int rightSum(int index, int size, int*arr) {
    int sum = 0;
    for (int i = index + 1; i <= (size - 1); i++)
        sum += arr[i];
    return sum;
}

int pivotIndex(int* nums, int numsSize){

    for (int i = 0; i < numsSize; i++) {
        int lSum = leftSum(i, nums);
        int rSum = rightSum(i, numsSize, nums);
                
        if (lSum == rSum)
            return i;
    }
    return -1;
}
