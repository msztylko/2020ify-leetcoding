/** 
 *   Forward declaration of guess API.
 *   @param  num   your guess
 *   @return        -1 if num is lower than the guess number
 *                   1 if num is higher than the guess number
 *                     otherwise return 0
 *   int guess(int num);
 **/

// Too slow
int guessNumber(int n) {
    if (n == 1) { return 1; }
    
    int pick = n/2; 
    int out = guess(pick);
    int interval = n/2;
    
    while (out != 0) {
        if (out == -1) {
            pick /= 2;
            out = guess(pick);
        } else if (out == 1) {
            interval = (interval / 2 == 0) ? 1 : interval/2 ;
            pick += interval; 
            out = guess(pick);
        }
    }
    return pick;
}
