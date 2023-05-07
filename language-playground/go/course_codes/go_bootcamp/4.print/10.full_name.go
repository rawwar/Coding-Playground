package main

import (
	"fmt"
	"os"
)

func main() {
	name, lastname := os.Args[1], os.Args[2]

	msg := "Your name is %s and your lastname is %s.\n"
	fmt.Printf(msg, name, lastname)
}
