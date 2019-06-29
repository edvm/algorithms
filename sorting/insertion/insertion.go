package main

import "fmt"
import "math/rand"

func getRandomNumberList(size int) []int {

	numbers := make([]int, size)

	for idx, _ := range numbers {
		numbers[idx] = rand.Intn(9)
	}

	return numbers
}

func sort(numbers []int) []int {

	for i := 1; i < len(numbers); i++ {

		key := numbers[i]
		j := i - 1

		for j >= 0 && numbers[j] > key {
			numbers[j+1] = numbers[j]
			j--
		}
		numbers[j+1] = key

	}

	return numbers
}

func main() {

	numbers := getRandomNumberList(30)
	fmt.Println("Generated a list of random numbers:", numbers)
	fmt.Println("Sorted list: ", sort(numbers))
}
