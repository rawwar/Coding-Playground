package main

import (
	"fmt"
	"os"
)

func main() {
	count := len(os.Args)
	fmt.Printf("There are %d names.\n", count)
}
