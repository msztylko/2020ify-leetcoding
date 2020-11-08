#include <stdlib.h>

int heightChecker(int* heights, int heightsSize) {    
    int *myArray = malloc(sizeof(int) * heightsSize);
    int counter = 0;
    int min;
    
    for (int i = 0; i < heightsSize; i++) {
        myArray[i] = heights[i];
    }
    
    for (int i = 0; i < heightsSize; i++) {
        min = i;
        for (int j = i + 1; j < heightsSize; j++) {
            if (myArray[j] < myArray[min]) {
                min = j;
            }
        }
        if (min != i) {
            int temp = myArray[i];
            myArray[i] = myArray[min];
            myArray[min] = temp;   
        }
    }
    
    for (int i = 0; i < heightsSize; i++) {
        if (myArray[i] != heights[i])
            counter++;
    }
    return counter;
}
