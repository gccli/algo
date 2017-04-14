#include <stdio.h>

void merge(int* nums1, int m, int* nums2, int n)
{
    int k = m+n-1;
    int i = m-1;
    int j = n-1;

    while (i>=0 && j>=0) {
        if (nums1[i] > nums2[j])
            nums1[k--] = nums1[i--];
        else
            nums1[k--] = nums2[j--];
    }

    while (k>=0) {
        nums1[k--] = (i>j) ? nums1[i--]:nums2[j--];
    }
}

int main(int argc, char *argv[])
{
    int i;
    int a1[10] = {1,5,8,10,13};
    int a2[5] = {2,4,7,10,11};

    merge(a1, 5, a2, 5);

    for(i=0; i<10; ++i) {
        printf("%d ", a1[i]);
    }
    printf("\n");
}
