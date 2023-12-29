package main

import "sort"

func NonConstructibleChange(coins []int) int {
	// Write your code here.
	res := 0
	sort.Ints(coins)
	for _, coin := range coins {
		if coin > res+1 {
			return res + 1
		}
		res += coin
	}
	return res + 1
}
