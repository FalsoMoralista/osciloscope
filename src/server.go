package main

import (
	"fmt"
	"math/rand"
	"net/http"
	"strconv"
	"time"
)

var buffer chan string

func main() {
	buffer = make(chan string, 10)
	go produce(buffer)
	http.HandleFunc("/", home)
	http.HandleFunc("/consume", consume)
	http.HandleFunc("/plot.js", plotScript)
	http.ListenAndServe(":8081", nil)
}

func produce(c chan string) {
	min := 0
	max := 5
	for {
		n := rand.Intn(max - min)
		c <- strconv.Itoa(n)
		println("produced: ", n)
		time.Sleep(1 * time.Second)
	}
}

func home(w http.ResponseWriter, req *http.Request) {
	w.Header().Set("Content-Type", "application/javascript")
	http.ServeFile(w, req, "plot.js")
}

func consume(w http.ResponseWriter, req *http.Request) {
	fmt.Fprintf(w, <-buffer)
	time.Sleep(1 * time.Second)
}

func plotScript(w http.ResponseWriter, req *http.Request) {
	w.Header().Set("Content-Type", "application/javascript")
	http.ServeFile(w, req, "plot.js")
}
