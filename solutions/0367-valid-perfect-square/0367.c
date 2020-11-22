#include <stdbool.h>

bool isPerfectSquare(int num) {
    if (num < 1) return false;
    if (num == 1) return true;
    
    long i = 1, square = 1;
    while (square < num) {
        i++;
        square = i*i;
    }
    return (square == num);
}
