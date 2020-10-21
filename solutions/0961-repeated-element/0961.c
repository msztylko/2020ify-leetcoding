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
