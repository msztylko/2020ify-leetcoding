int numPairsDivisibleBy60Naive(int* time, int timeSize){
    int counter = 0;
    
    for (int i = 0; i < timeSize; i++) {
        for (int j = i + 1; j < timeSize; j++) {
            if ((time[i] + time[j]) % 60 == 0)
                counter++;
        }
    }
    return counter;
}


int numPairsDivisibleBy60Hash(int *time, int timeSize) {
    int m[60] = {};
    int ret = 0;
    for (int i = 0; i < timeSize; i++) {
        int t = time[i] % 60;
        int y = (60 - t) % 60;
        ret += m[y];
        m[t]++;
    }
    return ret;
}
