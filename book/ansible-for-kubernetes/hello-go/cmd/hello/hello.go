package main

import (
    "fmt"
    "log"
    "net/http"
    "os"
)

// HelloServer responds to requests with the given URL
func HelloServer(w http.ResponseWriter, r *http.Request) {
    name, err := os.Hostname()
    if err != nil {
        panic(err)
    }
    fmt.Fprintf(w, "Hello! My name is %s. You requested %v", name, r.URL.Path)
    log.Printf("Received request for path: %s", r.URL.Path)
}

func main() {
    var addr string = ":8180"
    handler := http.HandlerFunc(HelloServer)
    if err := http.ListenAndServe(addr, handler); err != nil {
        log.Fatalf("Could not listen on port %s %v", addr, err)
    }
}
