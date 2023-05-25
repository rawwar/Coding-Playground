package main

import "fmt"

func main() {
	a, b := 10, 5.5
	// a = b
	// fmt.Println(a + b)

	// EXPECTED OUTPUT
	//  10.5
	a = int(b)
	fmt.Println(float64(a) + b)
}
