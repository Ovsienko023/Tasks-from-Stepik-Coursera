package main

import (
	"fmt"
	"strconv"
)

func main() {
	var (
		in string
		a  int64
		b  int64
		c  int64
		d  int64
		e  int64
		f  int64
	)

	fmt.Scan(&in)

	a, _ = strconv.ParseInt(string(in[0]), 0, 64)
	b, _ = strconv.ParseInt(string(in[1]), 0, 64)
	c, _ = strconv.ParseInt(string(in[2]), 0, 64)

	d, _ = strconv.ParseInt(string(in[3]), 0, 64)
	e, _ = strconv.ParseInt(string(in[0]), 0, 64)
	f, _ = strconv.ParseInt(string(in[0]), 0, 64)

	fmt.Print(a+b+c == d+e+f)

	if a+b+c == d+e+f {
		fmt.Print("YES")
	} else {
		fmt.Print("NO")
	}

}