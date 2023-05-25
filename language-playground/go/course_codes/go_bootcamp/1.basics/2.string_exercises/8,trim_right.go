package main

import (
	"fmt"
	"strings"
	"unicode/utf8"
)

func main() {
	// currently it prints 17
	// it should print 5
	name := "inanç           "
	fmt.Println(len(name))
	// updated
	fmt.Println(utf8.RuneCountInString(strings.TrimRight(name, " ")))
}
