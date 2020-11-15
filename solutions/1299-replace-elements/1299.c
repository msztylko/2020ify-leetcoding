#define MAX(a,b) (a>b) ? a : b

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

int* replaceElementsOptimized(int* arr, int arrSize, int* returnSize) {
    int max = -1;
    
    for (int i = arrSize - 1; i >= 0; i--) {
        int tmp = arr[i];
        arr[i] = max;
        max = MAX(tmp, max);
    }
    *returnSize = arrSize;
    return arr;
}
