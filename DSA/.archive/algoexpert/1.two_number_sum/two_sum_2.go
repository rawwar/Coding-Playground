package main

func TwoNumberSum(array []int, targetSum int) []int {
	nums := map[int]bool{}
	for _, num := range array {
		res := targetSum - num
		if _, found := nums[res]; found {
			return []int{res, num}
		}
		nums[num] = true
	}
	return []int{}
}