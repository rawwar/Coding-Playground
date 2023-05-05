package main

import "fmt"

func main() {
	color := "green"
	fmt.Println("Before: color is", color)
	color = "dark " + color
	fmt.Println("After: color is", color)
}
