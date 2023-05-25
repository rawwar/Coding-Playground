package main

import (
	"fmt"
	"math/rand"
	"os"
	"strconv"
	"time"
)

func main() {
	rand.Seed(time.Now().UnixNano())

	args := os.Args[1:]

	guess, err := strconv.Atoi(args[0])
	if err != nil {
		fmt.Println("Not a number.")
	}
	if 
}
