int repeatedNTimes(int* A, int ASize){
    int seen, i, j;
    
    for (i = 0; i < ASize-1; i++) {
        seen = A[i];
        for (j = i + 1; j < ASize; j++) {
            if (seen == A[j])
                return seen;
        }
    }
    return 0;
}

int repeatedNTimesHashTable(int* A, int ASize) {
    int hashTable[10000] = {0};
    
    for (int i = 0; i < ASize; i++) {
        hashTable[A[i]]++;
        if (hashTable[A[i]] > 1) {
            return A[i];
        }
    }
    return -1;
}
