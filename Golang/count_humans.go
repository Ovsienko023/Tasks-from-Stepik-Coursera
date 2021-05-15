package main

import (
	"bufio"
	"log"
	"os"
)

func countHuman(fileName string) (map[]){
	human := map[string]int{}

	file, err := os.Open(fileName)
	if err != nil {
		log.Fatal(err)
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
}
