package main

func SortedSquaredArray(array []int) []int {
	// Write your code here.
	low := 0
	high := len(array) - 1
	res := make([]int, len(array))

	for i := len(array) - 1; i >= 0; i-- {
		low_val := array[low]
		high_val := array[high]
		if abs(low_val) > abs(high_val) {
			res[i] = array[low] * array[low]
			low += 1
		} else {
			res[i] = array[high] * array[high]
			high -= 1
		}
	}
	return res
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}
