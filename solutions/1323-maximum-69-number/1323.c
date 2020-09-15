#include <math.h>

int maximum69Number (int num){
    int i = 0;
    int temp = num;
    int six_index = -1;
    
    while (temp > 0) {
        if (temp % 10 == 6) {
            six_index = i;
        }
        temp = temp / 10;
        i++;
    }
    
    return (six_index != -1) ? (num + 3 * pow(10, six_index)) : num;
}   
