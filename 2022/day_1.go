package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
)

type Elf struct {
	sumCalories int
}

func main() {
	elves := buildElves()
	var found_elf Elf
	for _, elf := range elves {
		if elf.sumCalories > found_elf.sumCalories {
			found_elf = elf
		}
	}

	fmt.Printf("Found elf with calories: %d\n", found_elf.sumCalories)

	sort.SliceStable(elves, func(i, j int) bool {
		return elves[i].sumCalories < elves[j].sumCalories
	})

	result := 0
	for i := len(elves) - 1; i >= len(elves)-3; i-- {
		result += elves[i].sumCalories
	}

	fmt.Printf("Total sum; top elves: %d\n", result)
}

func buildElves() []Elf {

	elves := []Elf{}

	f, err := os.Open("day_1_input.txt")

	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()

	scanner := bufio.NewScanner(f)

	elf := Elf{}
	for scanner.Scan() {
		calories, err := strconv.Atoi(scanner.Text())
		if err != nil {
			elves = append(elves, elf)
			elf = Elf{}
			continue
		}

		elf.sumCalories += calories
	}

	return elves

}
