int countNegatives(int** grid, int gridSize, int* gridColSize) {
    int counter = 0;
    
    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < *gridColSize; j++) {
            if (grid[i][j] < 0)
                counter++;
        }
    }
    return counter;
}
