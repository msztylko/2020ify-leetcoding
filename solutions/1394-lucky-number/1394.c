int findLucky(int* arr, int arrSize) {
    int hashmap[501] = {0};
    
    for (int i = 0; i < arrSize; i++) {
        hashmap[arr[i]]++;
    }
    int max = -1;
    for (int i = 0; i < arrSize; i++) {
        if (hashmap[arr[i]] == arr[i]) {
            if (arr[i] > max) {
                max = arr[i];
            }
        }
    }
    return max;
}
