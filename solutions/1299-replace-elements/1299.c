int* replaceElements(int* arr, int arrSize, int* returnSize){
    int max, i, j;
    
    for (i = 0; i <arrSize-1; i++) {
        max = 0;
        for (j = i + 1; j < arrSize; j++) {
            if(arr[j] > max)
                max = arr[j];
        }
        arr[i] = max;
    }
    arr[i] = -1;
    *returnSize = arrSize;
    return arr;
}
