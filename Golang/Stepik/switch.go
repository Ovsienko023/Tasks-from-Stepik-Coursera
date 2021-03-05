package main

import "fmt"

func main() {
	var in int

	fmt.Scan(&in)

	switch {
	case in > 0:
		fmt.Print("Число положительное")
	case in < 0:
		fmt.Print("Число отрицательное")
	case in == 0:
		fmt.Print("Ноль")
	}
}