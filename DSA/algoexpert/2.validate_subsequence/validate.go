package main

func IsValidSubsequence(array []int, sequence []int) bool {
	// Write your code here.
	i := 0
	for _, each := range array {
		if i == len(sequence) {
			break
		}
		if each == sequence[i] {
			i += 1
		}
	}
	return i == len(sequence)
}
