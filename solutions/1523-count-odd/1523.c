int countOddsNaive(int low, int high) {
    int counter = 0;
    
    for (int i = low; i <= high; i++) {
        if (i % 2 == 1) {
            counter++;    
        }
    }
    return counter;
}

int countOddsFast(int low, int high) {
    int counter = 0;
    
    if (low % 2 == 1) {    
        for (int i = low; i <= high; i += 2)
            counter++;
    } else {
        for (int i = low + 1; i <= high; i += 2) {
            counter++;
        }
    }
    return counter;
}

