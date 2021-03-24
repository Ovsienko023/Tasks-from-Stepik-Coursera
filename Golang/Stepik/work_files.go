package main

import (
	"bufio"
	"encoding/csv"
	"fmt"
	"io"
	"log"
	"os"
	"path/filepath"
)

type Files struct {
	file_name string
	region    string
}

func main() {
	dir, err := os.Getwd()
	if err != nil {
		log.Fatal(err)
	}

	files := pars_csv("people.csv")

	for i := 0; i < 4; i++ {
		create_fulder(files[i].region)
	}

	for i := 0; i < 4; i++ {
		name := files[i].file_name
		old_path := filepath.Join(dir, name)
		new_path := filepath.Join(dir, files[i].region, name)

		moveFile(old_path, new_path)
	}
}

func pars_csv(name_csv string) []Files {
	csvFile, _ := os.Open(name_csv)

	reader := csv.NewReader(bufio.NewReader(csvFile))
	var files []Files
	for {
		line, error := reader.Read()

		if error == io.EOF {
			break
		} else if error != nil {
			log.Fatal(error)
		}

		files = append(files, Files{
			file_name: line[0],
			region:    line[1],
		})

	}
	return files
}

func create_fulder(dir_name string) {
	if _, err := os.Stat(dir_name); os.IsNotExist(err) {
		err := os.Mkdir(dir_name, 0750)
		if err != nil {
			panic(err)
		}
	}

}

func moveFile(old_path string, new_path string) {
	err := os.Rename(old_path, new_path)
	if err != nil {
		fmt.Println(err)
		return
	}
}
