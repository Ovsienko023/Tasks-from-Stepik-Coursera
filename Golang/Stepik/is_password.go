package main

import (
	"fmt"
	"unicode"
)

func main() {
	var input string

	fmt.Scan(&input)
	password := []rune(input)

	if is_password(password) {
		fmt.Println("Ok")
	} else {
		fmt.Println("Wrong password")
	}
}

func is_password(password []rune) bool {
	if len(password) < 5 {
		return false
	}
	for i := range password {
		if len(password) < 5 {
			return false
		}
		if unicode.Is(unicode.Latin, password[i]) || unicode.Is(unicode.Number, password[i]) {
			continue
		} else {
			return false
		}
	}
	return true
}
