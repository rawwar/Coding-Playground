package main

import (
	"fmt"
	"path"
)

func main() {
	fullpath := "secret/file.txt"
	dir, _ := path.Split(fullpath)
	fmt.Println("Dir is", dir)
}
