package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"unicode"
)

func main() {
	var input string = "Быть или не быть."

	input, _ := bufio.NewReader(os.Stdin).ReadString('\n')

	input_lst := strings.Split(input, "")

	one_symbol := input_lst[0]
	last_symbol := input_lst[len(input_lst)-1]

	if strings.ToUpper(one_symbol) == one_symbol && last_symbol == "." {
		fmt.Println("Right")
	} else {
		fmt.Println("Wrong")
	}
}

func with_rune() {
	var input string = "Быть или не быть."

	var new_input = []rune(input)
	fmt.Println()
	if unicode.IsUpper(new_input[0]) && new_input[len(new_input)-1] == '.' {
		fmt.Println("Right")
	} else {
		fmt.Println("Wrong")
	}
}
