package main

import "fmt"

func main() {

	var (
		num   int
		chain int
		fin   int = 0
	)
	fmt.Scan(&num)

	for i := 0; i > num; i++ {
		fmt.Scan(&chain)
		if (chain > 9 && chain < 100) && chain%8 == 0 {
			fin += chain
		}

	}
	fmt.Print(fin)

}
