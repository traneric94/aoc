package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
	"time"
)

type board struct {
	grid [5][5]cell
}
type cell struct {
	value     int
	wasCalled bool
}

func timeTrack(start time.Time, name string) {
	fmt.Printf("Elapsed time for %s: %s\n", name, time.Since(start))
}

func parseInput() ([]int, []board) {
	file, err := os.Open("day_4_input.txt")
	if err != nil {
		fmt.Println("Error opening file" + err.Error())
	}
	defer file.Close()

	var numbersCalled []int
	var boards []board
	scanner := bufio.NewScanner(file)

	index := 0
	for scanner.Scan() {
		if index == 0 {
			numbersCalled = parseNumbersCalled(scanner.Text())
		} else {
			boards = append(boards, parseBoard(scanner))
		}
		index++
	}

	return numbersCalled, boards
}

func parseNumbersCalled(calledNumbers string) []int {
	var err error
	stringNumbersCalled := strings.Split(calledNumbers, ",")
	numbersCalled := make([]int, len(stringNumbersCalled))
	for index, stringNum := range stringNumbersCalled {
		numbersCalled[index], err = strconv.Atoi(stringNum)
		if err != nil {
			fmt.Println("Error parsing number" + err.Error())
		}
	}
	return numbersCalled
}

func parseBoard(scanner *bufio.Scanner) board {
	result_board := board{}
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

func processBoards(calledNumbers []int, boards []board) int {
	minTurnWin := math.MaxInt16
	var winningBoard *board
	for idx := range boards {
		currTurnWin := processBoard(calledNumbers, &boards[idx], minTurnWin)
		if minTurnWin > currTurnWin {
			minTurnWin = currTurnWin
			winningBoard = &boards[idx]
		}
	}
	if minTurnWin < len(calledNumbers) {
		return calculateResult(calledNumbers[minTurnWin], winningBoard)
	}

	fmt.Println("BREAKING")
	return 0
}

func processBoard(calledNumbers []int, board *board, min_turn_win int) int {
	for index, number := range calledNumbers {
		if index >= min_turn_win {
			return index
		} else {
			marked := markBoard(number, board)
			if marked && isWinningBoard(board) {
				return index
			}
		}
	}
	return min_turn_win
}

func isWinningBoard(board *board) bool {
	return isWinningRow(board) || isWinningCol(board)
}

func isWinningCol(board *board) bool {
	for i := 0; i < len(board.grid); i++ {
		if isWinningCurrentCol(board, i) {
			return true
		}
	}
	return false
}

func isWinningCurrentCol(board *board, colIdx int) bool {
	for _, row := range board.grid {
		if !row[colIdx].wasCalled {
			return false
		}
	}
	return true
}

func isWinningRow(board *board) bool {
	for i := range board.grid {
		if isWinningCurrentRow(&board.grid[i]) {
			return true
		}
	}
	return false
}

func isWinningCurrentRow(row *[5]cell) bool {
	for _, cell := range row {
		if !cell.wasCalled {
			return false
		}
	}
	return true
}

func calculateResult(winningNumber int, winningBoard *board) int {
	sum := 0
	for _, row := range winningBoard.grid {
		for _, cell := range row {
			if !cell.wasCalled {
				sum += cell.value
			}
		}
	}

	return sum * winningNumber
}
func markBoard(calledNumber int, board *board) bool {
	for i, row := range board.grid {
		for j, cell := range row {
			if cell.value == calledNumber {
				board.grid[i][j].wasCalled = true
				return true
			}
		}
	}
	return false
}

// Solution #2
// numbers called needs to processed into a map
// boards should be processed into something annoying else
func getResult(calledNumbers []int, boards []board) int {
	return 0
}
func main() {
	numbersCalled, boards := parseInput()
	fmt.Println(numbersCalled)
	defer timeTrack(time.Now(), "my_solution")
	fmt.Printf("Result: %d\n", processBoards(numbersCalled, boards))

	defer timeTrack(time.Now(), "my_solution")
	fmt.Printf("Result: %d\n", getResult(numbersCalled, boards))
}
