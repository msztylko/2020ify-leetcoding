void duplicateZeros(int* arr, int arrSize) {
    int possible_dups = 0;
    int length_ = arrSize - 1;
    
    for (int left = 0; left < length_ + 1; left++) {
        if (left > (length_ - possible_dups)) {
            break;
        }
        if (arr[left] == 0) {
            if (left == (length_ - possible_dups)) {
                arr[length_] = 0;
                length_ -= 1;
                break;
            }
            possible_dups++;
        }
    }
    int last = length_ - possible_dups;
    
    for (int i = last; i >= 0; i--) {
        if (arr[i] == 0) {
            arr[i + possible_dups] = 0;
            possible_dups--;
            arr[i + possible_dups] = 0;
        } else {
            arr[i + possible_dups] = arr[i];
        }
    }
}
