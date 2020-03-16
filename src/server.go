package main

import (
	"math/rand"
	"strconv"

	"golang.org/x/exp/io/i2c"
)

var buffer chan string

func main() {
	buffer = make(chan string, 10)
	go produce()
}

func produce() {
	min := 0
	max := 5
	for {
		n := rand.Intn(max - min)
		data := strconv.Itoa(n)
		buffer <- data
		// println("produced: ", n)
		// time.Sleep(50 * time.Millisecond)
	}
}

func consume() {
	var data = <-buffer
}

func openDeviceFile() {
	d, _ := i2c.Open(&i2c.Devfs{Dev: ""}, 0x39)
}
