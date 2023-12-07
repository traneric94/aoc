package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"

	"github.com/traneric94/aoc/utils"
)

func main() {
	var result int
	f, err := os.Open("day_2_input.txt")

	if err != nil {
		log.Fatal(err)
	}

	scanner := bufio.NewScanner(f)
	var game_product int

	// game_loop:
	for scanner.Scan() {
		game_product = 1
		game := strings.FieldsFunc(scanner.Text(), split)

		// gameId, err := strconv.Atoi(strings.Split(game[0], " ")[1])
		// if err != nil {
		// 	panic("invalid game id")
		// }

		limit := map[string]int{
			"red":   0,
			"green": 0,
			"blue":  0,
		}
		for _, turn := range game[1:] {
			for _, color := range strings.Split(turn, ",") {
				color_count := strings.Split(strings.Trim(color, " "), " ")

				count, err := strconv.Atoi(color_count[0])
				if err != nil {
					panic("invalid color count")
				}

				limit[color_count[1]] = utils.Max[int, int](limit[color_count[1]], count)

				// if limit[color_count[1]] < count {
				// 	continue game_loop
				// }

			}

		}
		for _, v := range limit {
			game_product *= v
		}
		// result += gameId
		// fmt.Printf("adding game id %v\n", gameId)
		result += game_product
	}

	fmt.Printf("Day 2: %v\n", result)
}

func split(r rune) bool {
	return r == ':' || r == ';'
}
