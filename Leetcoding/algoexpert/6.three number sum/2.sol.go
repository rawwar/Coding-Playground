package main

import "sort"

func ThreeNumberSum(array []int, target int) [][]int {
	// Write your code here.
	sort.Ints(array)
	triplets := [][]int{}
	for idx, num := range array {
		t := target - num

		l, r := idx+1, len(array)-1

		for l < r {
			total := array[l] + array[r]
			if total == t {
				triplets = append(triplets, []int{array[idx], array[l], array[r]})
				l += 1
				r -= 1
			} else if total < t {
				l += 1
			} else if total > t {
				r -= 1
			}
		}

	}

	return triplets
}
