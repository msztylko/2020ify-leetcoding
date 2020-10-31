int findSpecialInteger(int* arr, int arrSize) {
    if (arrSize < 2)
        return *arr;
    
    int percent = arrSize / 4;
    int counter;
    
    for (int i = 0; i < arrSize; i++) {
        counter = 1;
        for (int j = i + 1; j < arrSize; j++) {
            if (arr[i] == arr[j])
                counter++;
        }     
        if (counter > percent) {
            return arr[i];
        }
    }
    return 0;
}
