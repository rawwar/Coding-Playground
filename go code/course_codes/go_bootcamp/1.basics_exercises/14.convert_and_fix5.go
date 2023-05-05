package main

import "fmt"

func main() {
	min := int8(127)
	max := int16(1000)
	// EXPECTED OUTPUT
	//  1127
	fmt.Println(int16(min) + max)

}
