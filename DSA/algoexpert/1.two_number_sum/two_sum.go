package main

func TwoNumberSum(array []int, targetSum int) []int {
	for i := 0; i < len(array)-1; i++ {
		reqNum := targetSum - array[i]
		for j:=i+1; j < len(array); j++{
			if reqNum == array[j]{
				return []int{array[i], array[j]}
			}
		}
	}
	return []int{}
}
