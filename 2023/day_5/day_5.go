package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"

	"github.com/traneric94/aoc/utils"
)

type state struct {
	seed_id  int
	category string
	value    int
}

type mapping struct {
	source_start      int
	_range            int
	destination_start int
}

func main() {
	var result int

	parseInput(&states, &stateMachine, &mappings)

	fmt.Printf("states %v\n", states)
	fmt.Printf("stateMachine %v\n", stateMachine)
	fmt.Printf("mappings %v\n", mappings)
	// locationMapping := map[int]int{} // seed -> location

	var currState state
	for len(states) != 0 {
		currState, states = *states[0], states[1:]
		nextState := stateMachine[currState.category]

		for _, mapping := range mappings[stateMachine[nextState]] {
			if stateMachine[currState.category] == "location" {
				// locationMapping[currState.seed_id] = utils.Min[int, int](locationMapping[currState.seed_id], currState.value)
				result = utils.Min[int, int](result, currState.value)
				continue
			}

			states = append(states, &state{
				seed_id:  currState.seed_id,
				category: stateMachine[currState.category],
				value:    mapping.apply(currState.value),
			})
		}

	}
	fmt.Printf("Day 5: %d\n", result)
}

func (m *mapping) apply(source_position int) int {
	if source_position >= m.source_start && source_position < m._range {
		return source_position - m.source_start
	}
	return source_position
}

func parseInput() (states []state, stateMachine map[string]string, mappings map[string][]mapping) {
	states = make([]state, 0) // make vs {} less memory?
	stateMachine = map[string]string{}
	mappings = map[string][]mapping{}
	// instantiate here and then return?
	f, err := os.Open("day_5/day_5_input.txt")
	if err != nil {
		panic("error reading file")
	}

	scanner := bufio.NewScanner(f)

	i := -1
	var currState string
	for scanner.Scan() {
		i++
		row := scanner.Text()

		if row == "" {
			continue
		}

		if i == 0 {
			parseSeeds(states, row)
			continue
		}

		if strings.Contains(row, "map") {
			states := strings.Split(strings.Fields(row)[0], "-to-")
			// & -> referencing * deref
			// derefPtr := *stateMachine TODO check order of operations?
			(*stateMachine)[states[0]] = states[1]
			currState = states[1]
			continue
		}

		var nums []int
		for _, num := range strings.Fields(row) {
			number, err := strconv.Atoi(num)
			if err != nil {
				panic("error converting value")
			}

			nums = append(nums, number)
		}

		(*mappings)[currState] = append(
			(*mappings)[currState],
			mapping{
				destination_start: nums[0],
				source_start:      nums[1],
				_range:            nums[2],
			})
	}

}

func parseSeeds(states *[]*state, s string) {
	seeds := strings.Fields(strings.Split(s, ":")[1])
	fmt.Printf("seeds %s\n", seeds)
	for _, seed := range seeds[1:] {
		seed_id, err := strconv.Atoi(seed)
		if err != nil {
			panic("invalid seed id")
		}
		state := &state{
			seed_id:  seed_id,
			category: "seed",
			value:    seed_id,
		}
		stating := append(*states, state)
		states = &stating
		// states = append(*states, state)
		// testing := &[]string{}
	}
}
