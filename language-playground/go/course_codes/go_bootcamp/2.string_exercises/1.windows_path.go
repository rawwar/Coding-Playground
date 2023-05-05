package main

import "fmt"

func main() {
	path := "c:\\program files\\duper super\\fun.txt\n" +
		"c:\\program files\\really\\funny.png"
	fmt.Println(path)

	// using raw string literal

	path2 := `c:\program files\duper super\fun.txt
c:\program files\really\funny.png`
	fmt.Println(path2)

}
