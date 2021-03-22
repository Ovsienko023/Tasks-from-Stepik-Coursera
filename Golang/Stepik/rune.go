package main

import "fmt"

func main() {

	ExampleRune()
}

func ExampleRune() {
	// Поступим также, как в работе с типом []byte
	rs := []rune("Это срез рун")
	fmt.Println(rs)
	// Итерируясь мы будем заменять символ 'р' на '*'
	for i := range rs {
		if rs[i] == 'р' {
			// fmt.Println(rs[i], rs, i)
			rs[i] = '*'
		}
	}
	fmt.Println(rs)
	fmt.Printf("Измененнный срез в виде строки: %s\n", string(rs))

	// Output:
	// Измененнный срез в виде строки: Это с*ез *ун
}
