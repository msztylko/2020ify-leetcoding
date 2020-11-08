#include <stdbool.h>
#include <stdlib.h>

int absDiff(long int a, long int b) {
        return (a > b) ? a-b : b-a;
}

bool canMakeArithmeticProgression(int* arr, int arrSize) {
    int *myArray = malloc(sizeof(int) * arrSize);
    int d;

    for (int i = 0; i < arrSize; i++) {
        myArray[i] = arr[i];
    }
    
    for (int i = 0; i < arrSize; i++) {
        int min = i;
        for (int j = i + 1; j < arrSize; j++) {
            if (myArray[j] < myArray[min]) {
                min = j;
            }
        }
        int temp = myArray[i];
        myArray[i] = myArray[min];
        myArray[min] = temp;
    }
    d = absDiff(myArray[0], myArray[1]);
    for (int i = 0; i < arrSize - 1; i++) {
        if (absDiff(myArray[i], myArray[i+1]) != d) {
            return false;
        }
    }
    return true;
}
