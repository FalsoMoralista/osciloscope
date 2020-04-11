package main

import (
	"math/rand"
	"net"
	"strconv"
	"time"
)

var buffer chan string

// Generate random numbers between 0 & 5 and put them into a (channel) buffer.
// The process locks down when the buffer is full.
func produce() {
	min := 0
	max := 2
	for {
		n := rand.Intn(max - min)
		println(n)
		data := strconv.Itoa(n)
		buffer <- data
	}
}

// Consumes the data from the buffer.
// Process locks down when the buffer is cleared.
func send() {
	addr, err := net.ResolveTCPAddr("tcp", "127.0.0.1:7000")
	if err != nil {
		println("Erro de endereco")
		return
	}
	conn, err := net.DialTCP("tcp", nil, addr)
	if err != nil {
		println("Erro de conexao")
		return
	}
	for {
		var data = <-buffer
		conn.Write([]byte(data))
		time.Sleep(time.Millisecond * 500)
	}
}

// Allocates the buffer and starts threads to produce and consume respectively.
func main() {
	buffer = make(chan string, 100)
	go produce()
	go send()
	for {
	}
}
