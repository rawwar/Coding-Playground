package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	name := os.Args[1]
	msg := `hi $NAME$!
how are you?`
	msg = strings.Replace(msg, "$NAME$", name, -1)
	fmt.Println(msg)

	// concat
	msg2 := `hi ` + name + `!
how are you?`
	fmt.Println(msg2)
}
