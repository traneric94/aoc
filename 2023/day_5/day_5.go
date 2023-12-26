package main

import (
	"bufio"
	"errors"
	"fmt"
	"math"
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
	result := math.MaxInt

	states, stateMachine, mappings := parseInput()

	var currState state
	for len(states) != 0 {
		currState, states = states[0], states[1:]
		nextState := stateMachine[currState.category]

		if currState.category == "location" {
			result = utils.Min[int, int](result, currState.value)
			continue
		}

		newState := state{
			seed_id:  currState.seed_id,
			category: nextState,
			value:    currState.value,
		}

		var added bool
		for _, mapping := range mappings[nextState] {
			newStateValue, err := mapping.apply(currState.value)
			if err != nil {
				continue
			}
			newState.value = newStateValue

			added = true
			states = append(states, newState)
		}

		if !added {
			states = append(states, newState)
		}

	}
	fmt.Printf("Day 5: %d\n", result)
}

func (m *mapping) apply(source_position int) (int, error) {
	if source_position > m.source_start && source_position < m.source_start+m._range {
		return m.destination_start + source_position - m.source_start, nil
	}
	return 0, errors.New("not in range")
}

func parseInput() (states []state, stateMachine map[string]string, mappings map[string][]mapping) {
	states = make([]state, 0)
	stateMachine = make(map[string]string, 0)
	mappings = make(map[string][]mapping, 0)

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
			states = parseSeeds(row)
			continue
		}

		if strings.Contains(row, "map") {
			states := strings.Split(strings.Fields(row)[0], "-to-")
			stateMachine[states[0]] = states[1]
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

		mappings[currState] = append(
			mappings[currState],
			mapping{
				destination_start: nums[0],
				source_start:      nums[1],
				_range:            nums[2],
			})
	}

	return states, stateMachine, mappings
}

func parseSeeds(s string) (states []state) {
	seeds := strings.Fields(strings.Split(s, ":")[1])
	for _, seed := range seeds {
		seed_id, err := strconv.Atoi(seed)
		if err != nil {
			panic("invalid seed id")
		}
		state := state{
			seed_id:  seed_id,
			category: "seed",
			value:    seed_id,
		}
		states = append(states, state)
	}
	return
}
