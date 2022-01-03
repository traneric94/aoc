package main

import (
  "fmt"
  "bufio"
  "os"
  "log"
  "strings"
  "strconv"
)

type board interface {
}

type cell interface {
}

func parse_input() {}
func parse_board() {}

func getResult(numbersCalled []int, boards[]int) string {
  return "Hello"
}

func main() {
  fmt.Println("Hello World!")
  file, err := os.Open("day_4_input.txt")
  if err != nil {
    fmt.Println("Error opening file" + err.Error())
  }
  defer file.Close()

  scanner := bufio.NewScanner(file)
  index := 0
  var numbersCalled []int
  var boards []int
  for scanner.Scan() {
    if index == 0 {
      stringNumbersCalled := strings.Split(scanner.Text(), ",")
      numbersCalled = make([]int, len(stringNumbersCalled))
      for index, stringNum := range stringNumbersCalled {
        numbersCalled[index], err = strconv.Atoi(stringNum)
        if err != nil {
          fmt.Println("Error parsing number" + err.Error())
        }
      }
      fmt.Println("Numbers")
      fmt.Println(numbersCalled)
    }
    if index == 12 {
      break
    }

    board := []int
    fmt.Println(scanner.Text())

    if err := scanner.Err(); err != nil {
      log.Fatal(err)
      return
    }

    index++
  }

  fmt.Println(getResult(numbersCalled, boards))
}
