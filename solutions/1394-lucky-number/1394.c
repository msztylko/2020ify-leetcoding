int findLucky(int* arr, int arrSize) {
    int hashmap[501] = {0};
    
    for (int i = 0; i < arrSize; i++) {
        hashmap[arr[i]]++;
    }
    int max = 0;
    for (int i = 1; i < arrSize + 1; i++) {
        if (hashmap[i] == i) {
            if (i > max) {
                max = i;
            }
        }
    }
    return (max != 0) ? max : -1;
}

