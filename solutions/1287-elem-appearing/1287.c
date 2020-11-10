int findSpecialInteger(int* arr, int arrSize) {
    if (arrSize < 2) return *arr;
    
    int threshold = arrSize / 4;
    int counter = 1;
    
    for (int i = 0; i < arrSize - 1; i++) {
        if (arr[i] == arr[i+1]) {
            counter++;
            if (counter > threshold) {
                return arr[i];
            }
        } else {
            counter = 1;
        }
    }
    return 0;
}
