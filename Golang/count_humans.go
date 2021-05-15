package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func countHuman(fileName string) (map[string]int, error) {
	human := map[string]int{}

	file, err := os.Open(fileName)
	if err != nil {
		return nil, err
	}
	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		name := scanner.Text()
		human[name]++
	}

	err = file.Close()
	if err != nil {
		return nil, err
	}
	if scanner.Err() != nil {
		return nil, err
	}
	return human, nil
}

func main() {
	humans, err := countHuman("votes.txt")
	if err != nil {
		log.Fatal(err)
	} else {
		fmt.Println(humans)
	}
}
