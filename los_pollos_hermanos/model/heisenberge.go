package data

type Characters struct {
	ID         int
	Name       string
	Nickname   string
	Occupation string
	Status     string
	Image_url  string
}

type Quotes struct {
	ID           int
	Quote_text   string
	Character_id string
}

type Connections struct {
	Character1 int
	Character2 int
}

var Character = []*Characters{
	&Characters{
		ID:         1,
		Name:       "Walter White",
		Nickname:   "Heisenberg",
		Occupation: "Chemistry Teacher",
		Status:     "Married",
		Image_url:  "yoyooyoy.jpeg",
	},
	&Characters{
		ID:         2,
		Name:       "Jesse Pinkman",
		Nickname:   "bitch",
		Occupation: "U?nemployed",
		Status:     "Single",
		Image_url:  "jeseddd.jpeg",
	},
}

func (c *Characters) GetCharacters() []*Characters {
	return Character
}
