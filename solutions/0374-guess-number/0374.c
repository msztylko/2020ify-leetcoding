/** 
 *  * Forward declaration of guess API.
 *   * @param  num   your guess
 *    * @return          -1 if num is lower than the guess number
 *     *                  1 if num is higher than the guess number
 *      *               otherwise return 0
 *       * int guess(int num);
 *        */

int guessNumber(int n) {
    if (n == 1) { return 1; }
    
    int ans;
    
    int low = 1;
    int high = n;
    int mid, pick;

    while (low <= high) {
        mid = low + ((high - low) / 2);
        pick = mid;
        ans = guess(pick);
        
        if (ans == -1) {
            high = mid - 1;
        } else if (ans == 1) {
            low = mid + 1;
        } else {
            return pick;
        }
    }
    return -1;
}
