package main

import "fmt"

type Hero struct {
	On    bool
	Ammo  int
	Power int
}

func (a *Hero) Shoot() bool {
	if a.On == false {
		return false
	}
	if a.Ammo == 0 {
		return false
	} else {
		a.Ammo--
		return true
	}

}

func (a *Hero) RideBike() bool {
	if a.On == false {
		return false
	}
	if a.Power == 0 {
		return false
	} else {
		a.Power--
		return true
	}
}

func main() {
	testStruct := &Hero{true, 1, 2}
	fmt.Print(testStruct.Shoot())
}
