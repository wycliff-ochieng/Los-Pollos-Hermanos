package data

import data "github/wycliff-ochieng/los_pollos_hermanos/model"

type BreakingBadData struct {
	strg Storage
}

func NewBreakingBadData(strg Storage) *BreakingBadData {
	return &BreakingBadData{
		strg: strg,
	}
}

func (b BreakingBadData) GetAllCharacters() ([]data.Characters, error) {
	query := `SELECT * FROM characters`

	b.strg.QueryContext(ctx, query).Scan()
}
