package main

import (
	"fmt"
)

func merge(nums1 []int, m int, nums2 []int, n int) {
	var a = make([]int, m+n)
	var i int
	var j int
	var k int

	for i,j,k = 0,0,0; i < m && j < n; k++ {
		if nums1[i] < nums2[j] {
			a[k] = nums1[i]
			i++
		} else {
			a[k] = nums2[j]
			j++
		}
	}

	for ;j < n; k,j = k+1,j+1  {
		a[k] = nums2[j]
	}

	for ;i < m; k,i = k+1,i+1 {
		a[k] = nums1[i]
	}

	copy(nums1, a)

	fmt.Printf("%v\n", a)
}

func main() {
	var a2 = []int{1, 3, 5, 7, 9}

	var a1 = make([]int, 10)
	a1[0] = 1;
	a1[1] = 3;
	a1[2] = 5;
	a1[3] = 7;
	a1[4] = 10;
	fmt.Printf("merge array %v and %v\n", a1, a2)
	merge(a1, 5, a2, len(a2))
	fmt.Printf("%v\n", a1)
}
