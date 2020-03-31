package main

import (
	"math/rand"
	"strconv"
)

var buffer chan string

// Generate random numbers between 0 & 5 and put them into a (channel) buffer.
// The process locks down when the buffer is full. 
func produce() {
	min := 0
	max := 5
	for {
		n := rand.Intn(max - min)
		data := strconv.Itoa(n)
		buffer <- data
		println("produced: ", n)
	}
}

// Consumes the data from the buffer.
// Process locks down when the buffer is cleared.
func consume() { 
	for {
		var data = <-buffer // TODO: Send consumed data through a socket.
		println("Consumed", data)
	}
}

// Allocates the buffer and starts threads to produce and consume respectively.
func main() {
	buffer = make(chan string, 10)
	go produce()
	go consume()
}
