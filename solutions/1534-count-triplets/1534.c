int absDiff(int a, int b) {
    return (a > b) ? a-b : b-a;
}

int countGoodTriplets(int* arr, int arrSize, int a, int b, int c) {
    int counter = 0;
    for (int i = 0; i < arrSize; i++) {
        for (int j  = i + 1; j < arrSize; j++) {
            for (int k = j + 1; k < arrSize; k++) {
                if(absDiff(arr[i], arr[j]) <= a &&
                   absDiff(arr[j], arr[k]) <= b &&
                   absDiff(arr[i], arr[k]) <= c ){
                    counter++;
                }
            }
        }
    }
    return counter;
}
