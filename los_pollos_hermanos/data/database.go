package data

import (
	"database/sql"
	"log"
)

type Postgres struct {
	db *sql.DB
}

func NewPostgres(db *sql.DB) (*Postgres, error) {

	connStr := `` //connection details

	db, err := sql.Open("postgres", connStr)
	if err != nil {
		log.Fatalf("failed to open connection:%v", err)
		return nil, err
	}

	//ping
	if err := db.Ping();err != nil{
		log.Fatalf("DB connot be pinged")
		return nil, err
	}

	return &Postgres{}, nil
}

func (p *Postgres) Init() {}

func (p *Postgres) CreateCharactersTable() error {
	return nil
}

func (p *Postgres) CreateQuotesTable() error {
	return nil
}
