package main

import (
	"fmt"
)

func main() {
	var word string
	fmt.Scan(&word)

	word_run := []rune(word)
	res := []rune("")

	for i := len(word_run) - 1; i >= 0; i-- {
		res = append(res, word_run[i])
	}

	if string(word_run) == string(res) {
		fmt.Println("Палиндром")
	} else {
		fmt.Println("Нет")
	}

}
