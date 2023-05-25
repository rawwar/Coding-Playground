package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {

	if len(os.Args) != 2 {
		fmt.Println("Exactly one argument required")
	}

	num, err := strconv.Atoi(os.Args[1])

	if err != nil {
		fmt.Printf(`%q is not a integer\n`, os.Args[1])
	} else if num%2 == 0 {
		fmt.Printf("%d is an even number\n", num)
	} else if num%2 != 0 {
		fmt.Printf("%d is an odd number\n", num)
	}

}
