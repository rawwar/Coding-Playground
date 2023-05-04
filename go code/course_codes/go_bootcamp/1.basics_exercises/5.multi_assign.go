package main

import "fmt"

func main() {
	var (
		lang    string
		version int
	)
	lang, version = "go", 2
	fmt.Printf("Lang: %s, version: %d", lang, version)
}
