package main

import (
	"fmt"
	"os"
	"strings"
	"unicode/utf8"
)

func main() {
	msg := os.Args[1]
	l := utf8.RuneCountInString(msg)
	s := strings.Repeat("!", l) + msg + strings.Repeat("!", l)
	fmt.Println(s)
}
