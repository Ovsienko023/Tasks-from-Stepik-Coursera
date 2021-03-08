package main

import "fmt"

func main() {

	var input float64

	fmt.Scan(&input)
	if input > 10000 {
		fmt.Printf("%e", input)
		return
	}
	if input <= 0 {
		fmt.Printf("число %2.2f не подходит", input)
	} else {
		fmt.Printf("%.4f", input*input)
	}

}
