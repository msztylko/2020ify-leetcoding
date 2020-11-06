void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    int l_ptr = nums1Size - 1; 
    int n1_ptr = m - 1; 
    int n2_ptr = n - 1; 
    
    while(n2_ptr >=  0) {
        if(n1_ptr >= 0 && nums1[n1_ptr] > nums2[n2_ptr]) {
            nums1[l_ptr--] = nums1[n1_ptr--]; 
        }
        else { 
            nums1[l_ptr--] = nums2[n2_ptr--]; 
        }
    }
} 

