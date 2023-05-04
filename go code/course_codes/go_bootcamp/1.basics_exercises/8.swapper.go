package main

import "fmt"

func main() {
	color, color2 := "red", "blue"
	fmt.Printf("Before: color=%s, color2=%s", color, color2)
	color, color2 = color2, color
	fmt.Printf("\nAfter: color=%s, color2=%s", color, color2)

}
