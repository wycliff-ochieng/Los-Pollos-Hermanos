package data


type Characters struct{
	ID int
	Name string
	Nickname string
	Occupation string
	Status string
	Image_url string
}

type Quotes struct{
	ID int
	Quote_text string
	Character_id string
}

func NewCharacters()