package main

import "fmt"

func main() {
	age := 2
	// fmt.Println(int(7.5) + int(age))
	// EXPECTED OUTPUT
	//  9.5
	fmt.Println(7.5 + float64(age))
}
