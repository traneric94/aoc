package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func main() {

	f, err := os.Open("day_4_input.txt")
	if err != nil {
		panic("can't read file")
	}
	defer f.Close()

	// var result int
	scanner := bufio.NewScanner(f)

	for scanner.Scan() {
		row := scanner.Text()

		game := newGame(row)
		for k, _ := range game.winningNumbers {
			fmt.Printf("%d\n", k)

		}
		// fmt.Printf("GAME %v\n", game.winningNumbers)

		// result += game.calculateScore()
	}
}

type game struct {
	winningNumbers map[int]struct{}
	numbers        map[int]struct{}
}

func (g *game) calculateScore() int {
	var matches float64
	for k := range g.winningNumbers {
		if _, ok := g.numbers[k]; ok {
			matches++
		}
	}

	return int(math.Pow(2, matches))
}

func newGame(s string) (g game) {
	g.winningNumbers = make(map[int]struct{})
	g.numbers = make(map[int]struct{})

	splat := strings.FieldsFunc(s, split)
	for _, n := range strings.Fields(splat[1]) {
		num, err := strconv.Atoi(n)
		if err != nil {
			panic("not a number")
		}

		g.winningNumbers[num] = struct{}{}
	}
	for _, n := range strings.Fields(splat[2]) {
		num, err := strconv.Atoi(n)
		if err != nil {
			panic("not a number")
		}
		g.numbers[num] = struct{}{}
	}
	return g
}

func split(r rune) bool {
	return r == ':' || r == '|'
}
