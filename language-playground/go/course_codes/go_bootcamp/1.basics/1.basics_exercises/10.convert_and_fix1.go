package main

import "fmt"

func main() {
	a, b := 10, 5.5
	// Expected result is 15.5
	// fmt.Println(a + b)
	fmt.Println(float64(a) + b)
}
