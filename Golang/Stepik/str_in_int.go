// Например цифровой корень 65536 это 7 , потому что 6+5+5+3+6=25 и 2+5=7 .
package main

import (
	"fmt"
	"strconv"
)

func main() {
	var input string

	fmt.Scan(&input)

	for {
		input = sumString(input)

		if len(input) == 1 {
			fmt.Print(input)
			break
		}
	}
}

func sumString(input string) string {
	var sum int
	sum = 0

	for i := 0; i < len(input); i++ {
		num, _ := strconv.Atoi(string(input[i]))
		sum += num
	}

	return strconv.Itoa(sum)
}
