package main

import (
	"fmt"
)

func main() {
	var one string
	var two string

	fmt.Scan(&one, &two)

	one_rune := []rune(one)
	two_rune := []rune(two)

	for i := range one_rune {
		if i+len(two_rune) > len(one_rune) {
			fmt.Println(-1)
			break
		}
		if string(one_rune[i:i+len(two_rune)]) == string(two_rune) {
			fmt.Println(i)
			break
		}
	}
	// Вместо тысячи строк fmt.Println(strings.Index(x, s))
}
