package main

import (
	"fmt"
	"path"
)

func main() {
	// simple variable declaration
	var age int
	age = 10
	fmt.Println("Age is", age)

	// another way to declare variable
	another_age := 10
	fmt.Println("Again, Age is", another_age)

	// split path into dir and filename

	var dir, file string
	dir, file = path.Split("/usr/home/kalyan/file.txt")
	fmt.Println("File:", file, ";Directory:", dir)

	// discarding return values

	var file1 string
	_, file1 = path.Split("/usr/home/kalyan/file2.txt")
	fmt.Println("File name:", file1)
}
