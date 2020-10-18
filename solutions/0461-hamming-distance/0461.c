int hammingDistance(int x, int y) {
    int counter = 0;
    int z = x ^ y;
    while (z) {
        if (z % 2 != 0) {
            counter++;
        }
        z /= 2;
    }
    return counter;
}
