double average(int* salary, int salarySize){
    // min value from the constraints
    double min = 1000000.0 , max = 0.0;
    double sum = 0.0;
    
    for (int i = 0; i < salarySize; i++) {
        if (salary[i] < min)
            min = salary[i];
        if (salary[i] > max)
            max = salary[i];
        sum += salary[i];
    }
    return (sum - (min + max)) / (salarySize-2);
}
