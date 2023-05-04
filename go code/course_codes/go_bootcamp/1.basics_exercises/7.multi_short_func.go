package main

import "fmt"

func main() {
	a, b := multi()
	fmt.Println("a=", a, "; b=", b)
}

func multi() (int, int) {
	return 5, 6
}
