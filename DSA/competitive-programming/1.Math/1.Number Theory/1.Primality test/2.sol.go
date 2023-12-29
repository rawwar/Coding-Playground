package main

import (
	"fmt"
	"math"
)

func isPrime(n int) bool {
	if n <= 1 {
		return false
	}
	if n <= 3 {
		return true
	}
	if n%2 == 0 || n%3 == 0 {
		return false
	}

	sqrt := int(math.Sqrt(float64(n)))

	for i := 5; i*i < sqrt; i += 6 {
		if n%i == 0 || n%(i+2) == 0 {
			return false
		}
	}
	return true
}

func main() {

	number := 19

	if isPrime(number) {
		fmt.Println("Prime")
	} else {
		fmt.Println("Not Prime")
	}
}
