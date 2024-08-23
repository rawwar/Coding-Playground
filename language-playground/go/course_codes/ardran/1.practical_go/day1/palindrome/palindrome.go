package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {
	fmt.Println(isPalindrome("applppa"))
}

func isPalindrome(s string) bool {
	for i := 0; i < utf8.RuneCountInString(s)/2; i++ {
		if s[i] != s[utf8.RuneCountInString(s)-i-1] {
			return false
		}
	}
	return true
}
