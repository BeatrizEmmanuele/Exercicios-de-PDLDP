package main

import (
	"fmt"
)

func main(){

	var numbers [6]int
	var sumEven int
	var countOdd int

	fmt.Printf("Digite 6 números inteiros: ")

	for i := 0; i<6; i++{
		fmt.Scan(&numbers[i])
	} 

	fmt.Printf("Números pares digitados: ")
	for _, num := range numbers {
		if num%2 ==0{
			fmt.Printf(num, " ")
			sumEven += num
		}
	}
	fmt.Printf()

	fmt.Printf("Soma dos números pares:" , sumEven)

	fmt.Printf("Números ímpares digitados: ")
	for _, num := range numbers {
		if num%2 !=0{
			fmt.Printf(num, " ")
			countOdd++
		}
	}

	fmt.Printf("Quantidade de números ímpares: ", countOdd)
}