package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func buildInput() (map[string]int, []board) {
	file, err := os.Open("day_4_input.txt")
	if err != nil {
		fmt.Println("Error opening file" + err.Error())
	}
	defer file.Close()

	var numbersCalled map[string]int
	var boards []board
	scanner := bufio.NewScanner(file)

	index := 0
	for scanner.Scan() {
		if index == 0 {
			numbersCalled = parseCalls(scanner.Text())
		} else {
			boards = append(boards, buildBoard(scanner))
		}
		index++
	}

	return numbersCalled, boards
}

func buildBoard(scanner *bufio.Scanner) [][]string {
	result_board := [5][5]string
	i := 0
	for i < 5 {
		scanner.Scan()         // update scan pointer
		line := scanner.Text() // grab bytes at current pointer

		row := strings.Fields(line)
		for idx, val := range row {
			intVal, err := strconv.Atoi(val)
			if err != nil {
				fmt.Println("error converting string to int" + err.Error())
			}
			result_board.grid[i][idx] = cell{value: intVal}
		}
		i++
	}
	return result_board
}

func parseCalls(calledNumbers string) map[string]int {
	result := make(map[string]int, 100)
	stringNums := strings.Split(calledNumbers, ",")

	for idx, num := range stringNums {
		result[num] = idx
	}

	return result
}

func main() {

}
