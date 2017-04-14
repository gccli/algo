package main

import (
	"fmt"
)

func rotate(nums []int, k int) {
	n := len(nums)
	k = k % n
	n-k-1

	a := nums[k:]

	for i := 0; k > 0; i++ {
		nums[i], nums[n-k] = nums[n-k], nums[i]
		k--
	}
}

func main() {
	array := []int{1, 2, 3, 4, 5, 6, 7}
	fmt.Printf("%v\n", array)
	rotate(array, 3)
	fmt.Printf("%v\n", array)
}
