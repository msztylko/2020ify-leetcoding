void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    int ptr1 = m - 1;
    int ptr2 = n - 1;
    int index = nums1Size - 1;
    
    while (ptr2 >= 0) {
        if (ptr1 >= 0 && nums1[ptr1] > nums2[ptr2])
            nums1[index--] = nums1[ptr1--];
        else
            nums1[index--] = nums2[ptr2--];
    }
}
