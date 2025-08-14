package data

type Storage interface {
	GetAllCharacters() ([]model.Character, error)
	GetCharacterByName(name string) error
	GetRandomQuotes() ([]model.Quotes, error)
	GetAllConnections()
	GetCharacterIDByName(name string) (map[int]string, error)
	GetCharacterNameByID(ID int) (map[string]int, error)
}
