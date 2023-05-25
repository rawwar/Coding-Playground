package main

import "fmt"

func main() {
	json := "\n" +
		"{\n" +
		"\t\"Items\": [{\n" +
		"\t\t\"Item\": {\n" +
		"\t\t\t\"name\": \"Teddy Bear\"\n" +
		"\t\t}\n" +
		"\t}]\n" +
		"}\n"

	fmt.Println(json)

	json2 := `{
	"Items": [{
		"Item": {
			"name": "Teddy Bear"
		}
	}]
}`
	fmt.Println(json2)
}
