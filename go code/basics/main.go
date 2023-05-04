package main

import (
	"fmt"
	"os"
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

	// Another way
	_, file2 := path.Split("/usr/home/kalyan/file23.txt")
	fmt.Println("File name is :", file2)

	// Go read about Shadowing

	// type conversions
	speed := 100
	force := 2.5

	// We can't do speed = speed * force

	speed = int(float64(speed) * force)
	fmt.Println("Speed * force = ", speed)

	fmt.Printf("%#v\n", os.Args)
	numOfArgs := len(os.Args)
	fmt.Println("Number of cmd args=", numOfArgs)
}
