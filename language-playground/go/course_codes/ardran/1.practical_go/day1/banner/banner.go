package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {
	// s := "G🦋"
	// bytes := []byte{0x62, 0xF0, 0x9F, 0xA6, 0x8B}
	// s := string(bytes)
	// fmt.Println(len(s))
	// fmt.Println(s)
	// banner("Go", 30)
	banner("Go 🦋", 30)
	// for i, r := range s {
	// 	fmt.Println(i, r)

	// }
	// for k:=0; k<5; k++ {
	// 	y:= s[k]
	// 	fmt.Printf("-%c- of type %T\n", y, y)
	// }
}

func banner(text string, width int) {
	padding := (width - utf8.RuneCountInString(text)) / 2
	for i := 0; i < padding; i++ {
		fmt.Print(" ")
	}
	fmt.Println(text)
	for i := 0; i < width; i++ {
		fmt.Print("-")
	}
	fmt.Println()

}
