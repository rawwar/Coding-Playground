package main

import "fmt"

func main() {
	const (
		_ = iota
		Jan
		Feb
		Mar
	)
	fmt.Println(Jan, Feb, Mar)
}
