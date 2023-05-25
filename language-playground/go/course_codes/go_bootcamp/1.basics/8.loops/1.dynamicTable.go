package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Println("need only one argument :size")
	}
	num, err := strconv.Atoi(os.Args[1])
	if err != nil || num <= 0 {
		fmt.Printf(`%q is not a valid value`, os.Args[1])
	}
	fmt.Printf("%5s", "X")
	for i := 0; i <= num; i++ {
		fmt.Printf("%5d", i)
	}
	fmt.Println()

	for i := 0; i <= num; i++ {
		fmt.Printf("%5d", i)
		for j := 0; j <= num; j++ {
			fmt.Printf("%5d", i*j)
		}
		fmt.Println()
	}
}
