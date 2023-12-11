package main

import (
	"bufio"
	"fmt"
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

	var result int
	scanner := bufio.NewScanner(f)
	counter := map[int]int{} // counts game_id to copies

	for scanner.Scan() {
		row := scanner.Text()

		game := newGame(row)
		counter[game.id]++
		for matches := 1; matches <= game.countMatches(); matches++ {
			counter[game.id+matches] += counter[game.id]
		}
	}

	for _, count := range counter {
		result += count
	}

	fmt.Printf("Day 4: %d\n", result)
}

type game struct {
	id             int
	winningNumbers map[int]struct{}
	numbers        map[int]struct{}
}

// func (g *game) calculateScore() int {
// 	return int(math.Pow(2, float64(g.matchCount-1)))
// }

func (g *game) countMatches() (matches int) {
	for k := range g.winningNumbers {
		if _, ok := g.numbers[k]; ok {
			matches++
		}
	}

	return matches
}

func newGame(s string) (g game) {
	g.winningNumbers = make(map[int]struct{})
	g.numbers = make(map[int]struct{})

	splat := strings.FieldsFunc(s, split)
	id, err := strconv.Atoi(strings.Fields(splat[0])[1])
	if err != nil {
		panic("invalid game id")
	}

	g.id = id

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
