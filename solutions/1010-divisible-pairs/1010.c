/* This is not considered a “good” solution because 
 * better options exist, but it's a correct solution. */
int numPairsDivisibleBy60Naive(int* time, int timeSize) {
    int counter = 0;
    
    for (int i = 0; i < timeSize; i++) {
        for (int j = i + 1; j < timeSize; j++) {
            if ((time[i] + time[j]) % 60 == 0)
                counter++;
        }
    }
    return counter;
}

int numPairsDivisibleBy60Hash(int* time, int timeSize) {
    
    int counter = 0;
    int hashTable[60] = {0};
    
    for (int i = 0; i < timeSize; i++) {
        int t = time[i] % 60;
        // For t = 0 we couldn't index hashtable
        // without % 60 
        int y = (60 - t) % 60;
        counter += hashTable[y];
        hashTable[t]++;
    }
    return counter;
}
