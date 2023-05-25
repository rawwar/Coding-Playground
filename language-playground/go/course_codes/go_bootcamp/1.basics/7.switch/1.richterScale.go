package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Println("Need exactly one arguement")
		return
	}
	magnitude, err := strconv.ParseFloat(os.Args[1], 64)
	if err != nil {
		fmt.Printf(`%q is an invalid value`, os.Args[1])
		return
	}
	var desc string

	switch r := magnitude; {
	case r < 2:
		desc = "micro"
	case r >= 2 && r < 3:
		desc = "very minor"
	case r >= 3 && r < 4:
		desc = "minor"
	case r >= 4 && r < 5:
		desc = "light"
	case r >= 5 && r < 6:
		desc = "moderate"
	case r >= 6 && r < 7:
		desc = "strong"
	case r >= 7 && r < 8:
		desc = "major"
	case r >= 8 && r < 10:
		desc = "great"
	default:
		desc = "massive"
	}
	fmt.Printf("%.2f is %s\n", magnitude, desc)
}
