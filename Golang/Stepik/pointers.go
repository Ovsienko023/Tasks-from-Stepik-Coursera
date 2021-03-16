package main

import (
	"fmt"
)

func main() {
	var a int = 1
	var b *int = &a

	one(b)
	a++
	fmt.Println(a)
}

func one(a *int) {
	*a++
	fmt.Println(*a)
}
