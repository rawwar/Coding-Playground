package main

import (
	"fmt"
	"os"
	"unicode/utf8"
)

func main() {
	l := len(os.Args[1])
	fmt.Println("length is", l)

	// Above one only works for asic
	l2 := utf8.RuneCountInString(os.Args[1])
	fmt.Println("Actual length is", l2)
}
