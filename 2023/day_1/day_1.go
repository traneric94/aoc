package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"unicode"
)

func isDigit(s string) (string, error) {

	mapping := map[string]string{
		"one":   "1",
		"two":   "2",
		"three": "3",
		"four":  "4",
		"five":  "5",
		"six":   "6",
		"seven": "7",
		"eight": "8",
		"nine":  "9",
	}

	if digit, ok := mapping[s]; ok {
		return digit, nil
	}
	if len(s) == 1 && unicode.IsDigit(rune(s[0])) {
		return s, nil
	}

	return "", fmt.Errorf("not a digit")
}

func grabDigits(s string) int {
	number := ""

forward_out:
	for i := range s {
		for j := 0; j+i <= len(s); j++ {
			digit, err := isDigit(s[i : i+j])
			if err != nil {
				continue
			}
			number += digit
			break forward_out
		}
	}

backward_out:
	for i := len(s) - 1; i >= 0; i-- {
		for j := 0; j+i <= len(s); j++ {
			digit, err := isDigit(s[i : j+i])
			if err != nil {
				continue
			}
			number += digit
			break backward_out
		}
	}

	result, _ := strconv.Atoi(number)
	return int(result)
}

// func grabDigits(s string) int {
// 	number := ""

// 	for _, ch := range s {
// 		if unicode.IsDigit(ch) {
// 			number += string(ch)
// 			break
// 		}
// 	}

// 	for i := len(s) - 1; i >= 0; i-- {
// 		if unicode.IsDigit(rune(s[i])) {
// 			number += string(s[i])
// 			break
// 		}
// 	}

// 	result, _ := strconv.ParseInt(number, 10, 0)
// 	return int(result)
// }

func main() {

	f, err := os.Open("day_1_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	var result int
	for scanner.Scan() {
		result += grabDigits(scanner.Text())
	}
	fmt.Printf("Result: %d\n", result)
}
