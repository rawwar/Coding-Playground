package main

import "fmt"

func main() {
	n := 3.14 * 2
	fmt.Println("3.14 * 2 =", n)
	// Another way
	PI := 3.14
	multiplier := 2
	result := 0.0

	// need to convert multiplier to float64
	result = PI * float64(multiplier)
	fmt.Println("PI * multiplier=", result)
}
