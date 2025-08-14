package handlers

import (
	"log"
	"net/http"

	"github.com/wycliff-ochieng/los_pollos_hermanos/data"
)

type Alburquerquer struct {
	l *log.Logger
	st data.Storage
}

func NewAlburquerquer(l *log.Logger,strg data.Storage) *Alburquerquer {
	return &Alburquerquer{
		l:l,
		st:strg,
	}
}

func (a *Alburquerquer) GetCharacters(w http.ResponseWriter, r *http.Request) {
	a.l.Println("Fetching the charcter list....")





}

func (a *Alburquerquer) GetCharacterConnection(w http.ResponseWriter, r *http.Request){}