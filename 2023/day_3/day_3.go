package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"unicode"
)

func main() {

	f, err := os.Open("day_3_input.txt")

	if err != nil {
		panic("file not found")
	}

	var result int
	scanner := bufio.NewScanner(f)
	matrix := [140][140]rune{}
	visited := make(map[int]map[int]struct{})
	for i := 0; i < 140; i++ {
		visited[i] = make(map[int]struct{})
	}

	var i int
	for scanner.Scan() {
		text := scanner.Text()
		for j, cell := range text {
			matrix[i][j] = cell
		}
		i++
	}

	var inBounds = func(i, j int) bool {
		return 0 <= i && i < len(matrix) && 0 <= j && j < len(matrix[0])
	}

	// var foundNearbySymbol = func(i, j int) bool {
	// 	directions := [][2]int{{-1, -1}, {0, -1}, {-1, 0}, {1, 0}, {0, 1}, {1, 1}, {-1, 1}, {1, -1}}

	// 	for _, dir := range directions {
	// 		new_x, new_y := i+dir[0], j+dir[1]

	// 		if inBounds(new_x, new_y) && !(matrix[new_x][new_y] == '.' || unicode.IsDigit(matrix[new_x][new_y])) {
	// 			return true
	// 		}
	// 	}

	// 	return false
	// }

	// var traverse = func(i, j int) (int, bool) {
	// 	var k int
	// 	var foundSymbol bool
	// 	for k = j; k < len(matrix[0]) && unicode.IsDigit(matrix[i][k]); k++ {
	// 		if !foundSymbol && foundNearbySymbol(i, k) {
	// 			foundSymbol = true
	// 		}
	// 		visited[i][k] = struct{}{}
	// 	}

	// 	result, err := strconv.Atoi(string(matrix[i][j:k]))
	// 	if err != nil {
	// 		panic("not a number")
	// 	}

	// 	return result, foundSymbol
	// }

	var getNumber = func(i, j int) int {
		// expand left + right in bounds until we get a number
		k := j
		for ; 0 <= j && unicode.IsDigit(matrix[i][j]); j-- {
		}

		for ; k < len(matrix[0]) && unicode.IsDigit(matrix[i][k]); k++ {
		}

		result, err := strconv.Atoi(string(matrix[i][j+1 : k]))
		if err != nil {
			panic("not a number")
		}

		return result
	}
	var traverse = func(i, j int) int {

		directions := [][2]int{{-1, -1}, {0, -1}, {-1, 0}, {1, 0}, {0, 1}, {1, 1}, {-1, 1}, {1, -1}}
		gears := map[int]struct{}{}

		for _, dir := range directions {
			new_x, new_y := i+dir[0], j+dir[1]
			if inBounds(new_x, new_y) && unicode.IsDigit(matrix[new_x][new_y]) {
				num := getNumber(new_x, new_y)
				gears[num] = struct{}{}
			}

		}
		if len(gears) != 2 {
			return 0
		}

		result := 1
		for k := range gears {
			result *= k
		}
		return result
	}

	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[0]); j++ {
			if _, ok := visited[i][j]; !ok && matrix[i][j] == '*' {
				num := traverse(i, j)
				result += num
			}
		}
	}
	fmt.Printf("Day 3: %d\n", result)
}
