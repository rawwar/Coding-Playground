package main

import (
	"fmt"
	"os"
)

func main() {
	firstName, lastName := os.Args[1], os.Args[2]
	fmt.Printf("Full name is %s", firstName+" "+lastName)

}
