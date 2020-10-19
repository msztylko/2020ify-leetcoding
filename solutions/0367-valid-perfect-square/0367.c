#include <stdbool.h>

bool isPerfectSquare(int num){
    long result = 0, i=1;
    
    while (result < num) {
        result = i*i;
        i++;
    }
    return (result==num);
}
