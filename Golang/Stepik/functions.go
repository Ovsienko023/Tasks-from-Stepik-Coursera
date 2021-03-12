package main

import "fmt"

func main() {
	var age, name = add(4, 5, "Tom", "Simpson")
	fmt.Println(age)  // 9
	fmt.Println(name) // Tom Simpson
	var num = add2(1, 2)
	fmt.Print(num)
}

func add(x, y int, firstName, lastName string) (int, string) {
	var z int = x + y
	var fullName = firstName + " " + lastName
	return z, fullName
}

func add2(x, y int) int {
	return x + y
}
