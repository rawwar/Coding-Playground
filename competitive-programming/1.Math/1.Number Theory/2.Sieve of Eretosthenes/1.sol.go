package main

import "fmt"

func sieve(num int) []bool {
	primes := make([]bool, num+1)

	for i := 0; i <= num; i++ {
		if i < 2 {
			primes[i] = false
			continue
		}
		primes[i] = true
	}
	p := 2
	for p*p <= num {
		if primes[p] == true {
			for i := p * p; i <= num; i += p {
				primes[i] = false
			}
		}
		p++
	}
	return primes
}

func main() {
	num := 100
	primes := sieve(num)
	fmt.Println("Primes up to", num, ":")
	for idx, prime := range primes {
		if prime == true {
			fmt.Print(idx, " ")
		}
	}
}
