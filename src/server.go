package main

import (
	"encoding/json"
	"math/rand"
	"net/http"
	"strconv"
	"time"
)

type OsciloscopeData struct {
	Voltage string `json : "voltage"`
}

var buffer chan OsciloscopeData

func main() {
	buffer = make(chan OsciloscopeData, 10)
	go produce()
	http.HandleFunc("/", home)
	http.HandleFunc("/consume", consume)
	http.HandleFunc("/plot.js", plotScript)
	http.ListenAndServe(":8081", nil)
}

func produce() {
	min := 0
	max := 5
	for {
		n := rand.Intn(max - min)
		data := OsciloscopeData{Voltage: strconv.Itoa(n)}
		buffer <- data
		println("produced: ", n)
		time.Sleep(50 * time.Millisecond)
	}
}

func consume(w http.ResponseWriter, req *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	var data = <-buffer
	//	jsn, _ := json.Marshal(data)
	json.NewEncoder(w).Encode(data)
	//	fmt.Fprintf(w, string(json))
	//	time.Sleep(1 * time.Second)
}

func home(w http.ResponseWriter, req *http.Request) {
	w.Header().Set("Content-Type", "text/html")
	http.ServeFile(w, req, "index.html")
}

func plotScript(w http.ResponseWriter, req *http.Request) {
	w.Header().Set("Content-Type", "text/javascript")
	http.ServeFile(w, req, "plot.js")
}
