package main

import "log"

type APIServer struct {
	l    *log.Logger
	addr string
}

func NewAPIServer(l *log.Logger, addr string) *APIServer {
	return &APIServer{
		l:    l,
		addr: addr,
	}
}

func (s *APIServer) Run() {
	//setup router here
}
